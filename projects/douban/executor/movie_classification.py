#!/usr/bin/env python
# -*- coding: utf-8 -*-

from projects.douban.common.constants import Tag
from projects.douban.utils.clear_file_util import ClearFile
from projects.douban.utils.movie_datum_util import MovieDatum

from projects.douban.utils.output_util import OutputUtils


def get_classification(id):
    movie_items = MovieDatum.get_movie_etree(id)
    for item in movie_items:
        tag_lists = item['movie_info'].split('/')[2].strip()
        print('{}:{}'.format(item['title'], tag_lists) + "\n")
        for tag in tag_lists.split(' '):
            Tag.COUNT[tag] = Tag.COUNT.get(tag, 0) + 1
            Tag.SCORE[tag] = Tag.SCORE.get(tag, 0) + float(item['score'][0])


def main():
    # clear files
    ClearFile.clear_classification()

    # get classfication
    ids = [i * 25 for i in range(10)]
    for id in ids:
        get_classification(id)

    # output result
    OutputUtils.classification(sort_by_count=False)


if __name__ == '__main__':
    main()
