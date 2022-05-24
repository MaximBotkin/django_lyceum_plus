class FilterPostByTagMixin:
    tag_filter_name = "tag_filter"

    def apply_filter(self, posts, tag_filter):
        if tag_filter:
            posts = posts.filter(tags__name__in=[tag_filter])
        return posts
