__author__ = 'Jeffrey D.'
__version__ = '0.4'

from urllib.request import urlopen


def retrieve_link(url):
    """Returns HTML code for a particular url"""
    retrieve = urlopen(url)
    read = retrieve.read()
    html = read.decode('utf-8')
    return html


def retrieve_video_id(query):
    """Returns the YouTube video ID of the top search result for a query."""
    query = query.replace('\n', '')
    query = query.replace(' ', '+')
    query = query.replace('&', 'and')
    video_url = 'https://www.youtube.com/results?search_query={0}'.format(query)
    youtube_result = retrieveLink(video_url)
    begin = youtube_result.find('<ol id="search-results"') + 23
    begin = youtube_result.find('a href="', begin) + 8
    end = youtube_result.find('" class="', begin)
    begin = youtube_result.find('watch?v=', begin) + 8
    video_id = youtube_result[begin:end]
    if '&amp;list=' in video_id:  # handles when search returns a YT list.
        mark = video_id.find('&amp;list=')
        video_id = video_id[:mark]
    return video_id