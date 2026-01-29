from fsort.strategies.images import ImagesStrategy
from fsort.strategies.docs import DocsStrategy
from fsort.strategies.audio import AudioStrategy
from fsort.strategies.video import VideoStrategy
from fsort.strategies.archive import ArchiveStrategy
from fsort.strategies.fallback import FallbackStrategy
#from fsort.strategies.dummy import DummyStrategy

StrategyList = [ImagesStrategy, DocsStrategy, AudioStrategy, VideoStrategy, ArchiveStrategy, FallbackStrategy]
