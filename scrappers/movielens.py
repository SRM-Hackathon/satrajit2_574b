import re
import os




def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


def get_data(filename):
    with open(f'{filename}.html', 'r') as f:
        data = f.read()

    data = str(data)
    data = re.sub(r'<!---->', '', data)
    data = re.sub(r'\s+', ' ', data)
    scrapped_data = {}

    movie_cols = re.findall(r'<div class="col-md-6">(.*?)</div>', data)

    plot_summ = movie_cols[0]
    scrapped_data['plot_summary'] = re.findall(
        r'<p class="lead plot-summary">(.*?)</p>', plot_summ)[0].strip()

    movie_attr = movie_cols[1]
    movie_attr = re.findall(r'<li>(.*?)</li>', movie_attr)
    scrapped_data['year'] = movie_attr[0].strip()
    scrapped_data['duration'] = movie_attr[1].strip()

    expr_str = r'<a uisref="base.explore" href=".*?">(.*?)</a>'
    movie_lang = re.findall(
        r'<div class="heading-and-data"><div class="movie-details-heading">Languages</div>(.*?)</div>', data)[0]
    movie_directors = re.findall(
        r'<div class="heading-and-data"><div class="movie-details-heading">Directors</div>(.*?)</div>', data)[0]
    movie_cast = re.findall(
        r'<div class="heading-and-data"><div class="movie-details-heading">Cast</div>(.*?)</div>', data)[0]
    scrapped_data['languages'] = re.findall(expr_str, movie_lang)
    scrapped_data['directors'] = re.findall(expr_str, movie_directors)
    scrapped_data['cast'] = re.findall(expr_str, movie_cast)

    poster = re.findall(
        r'<div class="col-md-2"><h2 class="movie-details-sub-heading"> Poster </h2>(.*?)</div>', data)[0]
    scrapped_data['poster_url'] = re.findall(
        r'<img class="img-responsive rounded ml4-bordered" src="(.*?)">', poster)

    scrapped_data['image_urls'] = re.findall(
        r'<div class="col-md-4 col-sm-6 col-xs-12"><div class="movie-details-media-block"><a class="cursor-pointer"><img class="img-responsive rounded ml4-bordered" src="(.*?)"></a></div></div>', data)
    return scrapped_data
