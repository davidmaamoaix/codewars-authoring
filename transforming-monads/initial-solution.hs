module TransformingMonads where


-- to start off, let's define Functor and Applicative instances for Compose

newtype Compose f g a = Compose { runCompose :: f (g a) }

instance (Functor f, Functor g) => Functor (Compose f g) where
    fmap = undefined

instance (Applicative f, Applicative g) => Applicative (Compose f g) where
    pure = undefined
    (<*>) = undefined


-- definitions of transformers

newtype IdentityT m a = IdentityT { runIdentity :: m a } deriving Show
newtype MaybeT m a = MaybeT { runMaybe :: m (Maybe a) } deriving Show
newtype ListT m a = ListT { runList :: m [a] } deriving Show
newtype StateT s m a = StateT { runStateT :: s -> m (a, s) } deriving Show
newtype ReaderT r m a = ReaderT {runReader :: r -> m a } deriving Show
newtype WriterT w m a = WriterT { runWriter :: m (a, w) } deriving Show
newtype EitherT e m a = EitherT { runEither :: m (Either e a) } deriving Show


-- the IdentityT monad has already been defined for you

instance Functor m => Functor (IdentityT m) where
  fmap f = IdentityT . fmap f . runIdentity
  
instance Applicative m => Applicative (IdentityT m) where
  pure = IdentityT . pure
  IdentityT f <*> IdentityT a = IdentityT $ f <$> a
  
instance Monad m => Monad (IdentityT m) where
  IdentityT a >>= f = IdentityT $ a >>= f


-- MaybeT
  
instance Functor m => Functor (MaybeT m) where
  fmap = undefined
  
instance Applicative m => Applicative (MaybeT m) where
  pure = undefined
  (<*>) = undefined
  
instance Monad m => Monad (IdentityT m) where
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
  
instance Functor m => Functor (Reader r m) where
  fmap = undefined
  
instance Applicative m => Applicative (Reader r m) where
  pure = undefined
  (<*>) = undefined
  
instance Monad m => Monad (Reader r m) where
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
  
instance Functor m => Functor (Either e m) where
  fmap = undefined
  
instance Applicative m => Applicative (Either e m) where
  pure = undefined
  (<*>) = undefined
  
instance Monad m => Monad (Either e m) where
  (>>=) = undefined
  