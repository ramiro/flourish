from flourish.generators import (
    AtomGenerator,
    IndexGenerator,
    PageGenerator,
    PaginatedIndexGenerator,
)
from flourish.helpers import publication_range


class NewestFirstIndex(IndexGenerator):
    order_by = ('-published')


class OnePageIndex(IndexGenerator):
    limit = 1


class FourPagePaginatedIndex(PaginatedIndexGenerator):
    order_by = ('published')
    per_page = 4


def global_context(self):
    return {
        'copyright_year_range': publication_range(self.flourish),
    }

GLOBAL_CONTEXT = global_context

SOURCE_URL = (
    '/#slug',
    PageGenerator.as_generator(),
)


URLS = (
    (
        '/',
        'homepage',
        NewestFirstIndex.as_generator(),
    ),
    (
        '/tags/#tag/',
        'tags-tag-page',
        OnePageIndex.as_generator(),
    ),
    (
        '/index.atom',
        'atom-feed',
        AtomGenerator.as_generator(),
    ),
    (
        '/tags/#tag/index.atom',
        'tags-atom-feed',
        AtomGenerator.as_generator(),
    ),
    (
        '/all/',
        'all-paginated',
        FourPagePaginatedIndex.as_generator(),
    ),
)
