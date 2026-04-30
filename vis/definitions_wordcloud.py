# Code based on gallery example for wordcloud library found at:
#     https://amueller.github.io/word_cloud/auto_examples/
#     colored.html#sphx-glr-auto-examcples-colored-py
#
# Image from:
#     https://society-rse.org/trademark-and-logo-policy/

# Requires libraries for the imports below, notably PIL, yaml and wordcloud

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

import yaml

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()


def parse_all_definitions():
    """Get all word definitions from the YAML defintions."""
    with open("dummy_yaml/dummy_definitions.yaml", "r") as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)

    # Print the values as a dictionary
    print("All YAML data is:", data)
    data = data
    all_defs = []
    for item in data:
        if "definition" in item:
            all_defs.append(item["definition"])

    print("All definitions pulled from the YAML are:", all_defs)

    return all_defs


def generate_wordcloud(text):
    """Generates a word cloud of input text."""

    # read the mask / color image
    alice_coloring = np.array(
        Image.open(path.join(d, "images/rse_logo_crop_white_background.png")))
    stopwords = set(STOPWORDS)
    stopwords.add("said")

    wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
                   stopwords=stopwords, max_font_size=40, random_state=42)
    # generate word cloud
    wc.generate(text)

    # create coloring from image
    image_colors = ImageColorGenerator(alice_coloring)

    # show
    fig, axes = plt.subplots(1, 2)
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    axes[0].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    axes[1].imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
    for ax in axes:
        ax.set_axis_off()
    plt.show()
    fig.savefig("images/definitions_word_cloud.png")


if __name__ == "__main__":
    definitions = parse_all_definitions()

    # Convert list of definitions to a merged string
    defs_combined = " ".join(definitions)

    generate_wordcloud(defs_combined)
