import re
import json


def save_scrap(filename):
    with open(f'{filename}.html', 'r') as f:
        file_data = f.read()

    file_data = str(file_data)
    file_data = re.sub(r'\s+', ' ', file_data)
    matches = re.findall(
        r'<div draggable="true"><li class="tracklist-row" role="button" tabindex="0">(.*?)</li></div>', file_data)

    parsed_data = []

    for match in matches:
        artists = re.findall(
            r'<span draggable="true"><a tabindex="-1" class="tracklist-row__artist-name-link" href="(.*?)">(.*?)</a></span>', match)
        album = re.findall(
            r'<a tabindex="-1" class="tracklist-row__album-name-link" href="(.*?)">(.*?)</a>', match)[0]
        track_name = re.findall(
            r'<div class="tracklist-name ellipsis-one-line" dir="auto">(.*?)</div>', match)[0]
        track_len = re.findall(
            r'<div class="tracklist-duration tracklist-top-align"><span>(.*?)</span></div>', match)[0]

        artists_dicts = [{
            'link': artist[0],
            'name': artist[1]
        } for artist in artists]

        parsed_data.append({
            'track_name': track_name,
            'album': {
                'link': album[0],
                'name': album[1],
            },
            'artists': artists_dicts,
            'track_len': track_len,
        })

    with open(f'converted_{filename}.json', 'w') as f:
        json.dump(parsed_data, f)
