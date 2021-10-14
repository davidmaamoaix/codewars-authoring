_This kata aims to teach you the basics of monad transformers, what they are, and why they are useful._

Monads are useful and fun. However, there are times when a single monad just isn't enough; what if you want a list of `Maybe`? Perhaps a `State` that produces a `Reader`?

The composition of functors are easy; all you do is defined a composition functor:

```haskell
newtype Compose f g a = Compose { runCompose :: (f (g a)) }
```

Now define `Functor` and `Applicative` instances for `Compose`! I'm sure that's trivial for an amazing code warrior like you.

With the new `Compose` of functors, we got to do stuff like this:

```haskell
addToListOfMaybeInt :: Int -> Compose [] Maybe Int -> Compose [] Maybe Int
addToListOfMaybeInt n a = (+ n) <$> a
```

As you can see, with the composed functor, we can penetrate two functors with a single `fmap`, effectively making nested functors much easier to operate on.

Now let's do the same with `Monad`!

```haskell
instance (Monad f, Monad g) => Monad (Compose f g) where
```

Well, `return` just lifts a value into a minimal context. That's equivalent to `pure`:

```haskell
return = pure
```

Easy! Now let's try defining bind: `(>>=)`...
```haskell
-- (>>=) :: Compose f g a -> (a -> Compose f g b) -> Compose f g b
Compose a >>= t = ???
```

Wait a minute... I can't think of a way to do so without breaking polymorphism! Maybe we are going the wrong way? Let's try defining `join` instead. `join` is isomorphic to `bind`, so if we have a definition for `join` with `Compose`, we can surely define `bind`!

```haskell
joinC :: (Monad f, Monad g) => Compose f g (Compose f g a) -> Compose f g a

-- which is essentially:
-- join :: (Monad f, Monad g) => f (g (f (g a))) -> f (g a)
```

_Curses!_ There is no way to define such as function. `f` and `g` are monoids in the category of endofunctors, and can therefore join with themselves (monads forms a monoid under the binary operation `join`). We can join `f (f a)` and end up with `f a`, but there is no way to join across a composed monad (at least when keeping both `f` and `g` polymorphic)!

Hmm... But if we know _one_ of either `f` or `g`, we can then join the compositions together. In other words, for a monad composition `Compose f g`, we can define `join`  if one of `f` or `g` is concrete.

Let's try with fixing `g` to `Maybe` first (`-XScopedTypeVariables` is enabled for type clarity):
```haskell
bindMaybeC :: forall f a b. Monad f => Compose f Maybe a -> (a -> Compose f Maybe b) -> Compose f Maybe b
bindMaybeC (Compose a) f = Compose $ a >>= inner
    where
        inner :: Maybe a -> f (Maybe b)
        inner Nothing = pure Nothing
        inner (Just a) = runCompose $ f a

joinMaybeC :: forall f a. Monad f => Compose f Maybe (Compose f Maybe a) -> Compose f Maybe a
joinMaybeC (Compose a) = Compose $ a >>= inner
    where
        inner :: Maybe (Compose f Maybe a) -> f (Maybe a)
        inner Nothing = pure Nothing
        inner (Just (Compose m)) = m >>= core
        core :: Maybe a -> f (Maybe a)
        core Nothing = pure Nothing
        core (Just m) = pure $ Just m
```

This might be a bit confusing at first; feel free to stare at the types a bit more.

And that's essentially what a monad transformer is! With the above definition, we can treat compositions such as `Compose [] Maybe` like a normal monad (but using `bindMaybeC` instead of `(>>=)` at the moment).

In the real world, monad transformers are defined a bit differently. Instead of using a `Compose` type, we have a different constructor for each monad transformer. For example, the `MaybeT` transformer for the `Maybe` monad is defined:
```haskell
newtype MaybeT m a = MaybeT { runMaybeT :: m (Maybe a) }
```

And of course, its definition as instance of `Functor`, `Applicative` and `Monad`:
```haskell
instance (Functor m) => Functor (MaybeT m) where
  -- blah blah blah
  
instance (Applicative m) => Applicative (MaybeT m) where
  -- blah blah blah
  
instance (Monad m) => Monad (MaybeT m) where
  -- blah blah blah
```

Therefore, something like `MaybeT IO Int` is equivalent to `Compose IO Maybe Int` with our previous composition. Note the order of type parameters for a transformer though.

With that out of the way, your task for this kata is to define some basic monad transformers:
```haskell
newtype IdentityT m a = IdentityT { runIdentity :: m a }
newtype MaybeT m a = MaybeT { runMaybe :: m (Maybe a) }
newtype ListT m a = ListT { runList :: m [a] }
newtype StateT s m a = StateT { runStateT :: s -> m (a, s) }
newtype ReaderT r m a = ReaderT {runReader :: r -> m a }
newtype WriterT w m a = WriterT { runWriter :: m (a, w) }
newtype EitherT e m a = EitherT { runEither :: m (Either e a) }
```

Then, you will define some basic operations on certain monad transformers, as well as write some operations and utilize your shiny new transformers.

Good luck!

## Notes
- Just for fun: composing a monad transformer with the `Identity` monad gives back the monad represented by the transformer (e.g. `MaybeT Identity` is equivalent to `Maybe`).
