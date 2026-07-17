from axion.oracle.vision.image import ImageLoader
from axion.oracle.vision.analyzer import ScreenAnalyzer


loader = ImageLoader()

frame = loader.load(
    ".axion/reports/screenshot_20260717_175834.png"
)


analyzer = ScreenAnalyzer()

state = analyzer.analyze(
    frame
)


print(state)