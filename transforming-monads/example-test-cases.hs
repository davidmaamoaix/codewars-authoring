module TransformingMonadsSpec where

import Test.Hspec
import Test.Hspec.Codewars

hiddenModules :: [Hidden]
hiddenModules = FromModule "Control.Monad.Trans" <$> trans
  where
    trans = [ "IdentityT", "MaybeT", "ListT"
            , "StateT" , "ReaderT" , "WriterT"
            , "ExceptT"
            ]

spec :: Spec
spec = do
  describe "No cheating" $ do
    it "No Control.Monad.Trans" $ solutionShouldHideAll hiddenModules
    