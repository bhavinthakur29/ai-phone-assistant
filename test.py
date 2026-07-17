from axion.oracle.android.ui import (
    AndroidUI,
    UIAnalyzer,
)


ui = AndroidUI()


elements = ui.dump()


print(
    "Elements:",
    len(elements)
)


analyzer = UIAnalyzer()


summary = analyzer.summarize(
    elements
)


print(
    summary
)


print("\nClickable elements:\n")


for element in analyzer.clickable_elements(elements):

    print(
        {
            "text": element.text,
            "resource_id": element.resource_id,
            "class": element.class_name,
            "bounds": element.bounds,
            "center": element.center,
        }
    )