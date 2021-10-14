module TransformingMonads where


-- to start off, let's define Functor and Applicative instances for Compose

newtype Compose f g a = Compose { runCompose :: f (g a) }

instance (Functor f, Functor g) => Functor (Compose f g) where
    fmap = undefined

instance (Applicative f, Applicative g) => Applicative (Compose f g) where
    pure = undefined
    (<*>) = undefined


-- definitions of transformers

newtype IdentityT m a = IdentityT { runIdentity :: m a }
newtype MaybeT m a = MaybeT { runMaybe :: m (Maybe a) }
newtype ListT m a = ListT { runList :: m [a] }
newtype StateT s m a = StateT { runStateT :: s -> m (a, s) }
newtype ReaderT r m a = ReaderT {runReader :: r -> m a }
newtype WriterT w m a = WriterT { runWriter :: m (a, w) }
newtype EitherT e m a = EitherT { runEither :: m (Either e a) }


-- the IdentityT monad has already been defined for you

instance Functor m => Functor (IdentityT m) where
  fmap f = IdentityT . fmap f . runIdentity
  
instance Applicative m => Applicative (IdentityT m) where
  pure = IdentityT . pure
  IdentityT f <*> IdentityT a = IdentityT $ f <*> a
  
instance Monad m => Monad (IdentityT m) where
  IdentityT a >>= f = IdentityT $ a >>= (runIdentity . f)


-- MaybeT
  
instance Functor m => Functor (MaybeT m) where
  fmap = undefined
  
instance Applicative m => Applicative (MaybeT m) where
  pure = undefined
  (<*>) = undefined
  
instance Monad m => Monad (MaybeT m) where
  (>>=) = undefined
  
  
-- ListT
  
instance Functor m => Functor (ListT m) where
  fmap = undefined
  
instance Applicative m => Applicative (ListT m) where
  pure = undefined
  (<*>) = undefined
  
instance Monad m => Monad (ListT m) where
  (>>=) = undefined
  
  
-- StateT
  
instance Functor m => Functor (StateT s m) where
  fmap = undefined
  
instance Applicative m => Applicative (StateT s m) where
  pure = undefined
  (<*>) = undefined
  
instance Monad m => Monad (StateT s m) where
  (>>=) = undefined
  
  
-- ReaderT
  
instance Functor m => Functor (ReaderT r m) where
  fmap = undefined
  
instance Applicative m => Applicative (ReaderT r m) where
  pure = undefined
  (<*>) = undefined
  
instance Monad m => Monad (ReaderT r m) where
  (>>=) = undefined
  
  
-- WriterT
  
instance Functor m => Functor (WriterT w m) where
  fmap = undefined
  
instance Applicative m => Applicative (WriterT w m) where
  pure = undefined
  (<*>) = undefined
  
instance Monad m => Monad (WriterT w m) where
  (>>=) = undefined
  

-- EitherT (this is called ExceptT in Control.Monad.Trans)
  
instance Functor m => Functor (EitherT e m) where
  fmap = undefined
  
instance Applicative m => Applicative (EitherT e m) where
  pure = undefined
  (<*>) = undefined
  
instance Monad m => Monad (EitherT e m) where
  (>>=) = undefined
  