def imshow(image, click_event=None, cmap=None):
    """
    Show an image at true scale
    """
    import matplotlib.pyplot as plt
    dpi = 80
    margin = 0.5  # (5% of the width/height of the figure...)
    h, w = image.shape[:2]

    # Make a figure big enough to accomodate an axis of xpixels by ypixels
    # as well as the ticklabels, etc...
    figsize = (1 + margin) * w / dpi, (1 + margin) * h / dpi

    fig = plt.figure(figsize=figsize, dpi=dpi)
    # Make the axis the right size...
    ax = fig.add_axes([0, 0, 1, 1])

    ax.imshow(image, interpolation='none', cmap=cmap)
    
    plt.axis('off')
    plt.show()
    
    return fig, ax
   
def get_sed_model_file():
    import os.path
    default_path = 'data/opencv_sed_model.yml.gz'
    if os.path.isfile(default_path):
        return default_path
    else:
        import urllib.request as request
        dl_path = './opencv_sed_model.yml.gz'
        request.urlretrieve('https://github.com/higra/Higra-Notebooks/raw/master/data/opencv_sed_model.yml.gz', dl_path)
        return dl_path
    
def locate_resource(name):
    import os.path
    default_path = 'data/' + name
    if os.path.isfile(default_path):
        return default_path
    else:
        return 'https://github.com/higra/Higra-Notebooks/raw/master/data/' + name
    
def enable_plotly_in_cell():
    """
    To be used in colab: this method pre-populates the outputframe with the configuration that Plotly expects 
    and must be executed for every cell which is displaying a Plotly graph.
    
    https://colab.research.google.com/notebooks/charts.ipynb#scrollTo=niTJd49yO4xf
    """
    import IPython
    from plotly.offline import init_notebook_mode
    display(IPython.core.display.HTML('''
        <script src="/static/components/requirejs/require.js"></script>
    '''))
    init_notebook_mode(connected=False)