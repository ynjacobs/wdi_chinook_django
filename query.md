>>> queen = Artist.objects.get(name='Queen')
>>> Album.objects.filter(artist= queen)
<QuerySet [<Album: Album object (32)>, <Album: Album object (181)>, <Album: Album object (182)>]>
>>> [al.title for al in Album.objects.filter(artist= queen)]
['Greatest Hits II', 'Greatest Hits I', 'News Of The World']
>>> Album.objects.get(artist= 51)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/query.py", line 412, in get
    (self.model._meta.object_name, num)
chinook.models.Album.MultipleObjectsReturned: get() returned more than one Album -- it returned 3!
>>> Artist.objects.filter(name='Queen')
<QuerySet [<Artist: Artist object (51)>]>
>>> Album.objects.filter(artist= 51)
<QuerySet [<Album: Album object (32)>, <Album: Album object (181)>, <Album: Album object (182)>]>
>>> MediaType.objects.filter(name='Protected MPEG-4 video file').count()
1
>>> Genre.objects.get(name= 'Hip Hop/Rap')
<Genre: Genre object (17)>
>>> Genre.objects.get(name= 'Hip Hop/Rap').name
'Hip Hop/Rap'
>>> Track.objects.filter(genre= 17).count()
35
>>> from django.db.models import Avg, Sum, Max, Min
>>> Track.objects.aggregate(Sum('milliseconds'))
{'milliseconds__sum': 1377942652}
>>> Track.objects.aggregate(Sum('milliseconds')) /1000
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'dict' and 'int'
>>> int(Track.objects.aggregate(Sum('milliseconds'))) / 1000
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: int() argument must be a string, a bytes-like object or a number, not 'dict'
>>> Track.objects.aggregate(Sum('milliseconds'))
{'milliseconds__sum': 1377942652}
>>> Track.objects.aggregate(Sum('milliseconds')).next
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'next'
>>> Track.objects.aggregate(Sum('milliseconds'))
{'milliseconds__sum': 1377942652}
>>> Track.objects.aggregate(Max('unit_price'))
{'unit_price__max': Decimal('1.99')}
>>> Media.objects.filter(name= 'MPEG audio file')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'Media' is not defined
>>> MediaType.objects.filter(name= 'MPEG audio file')
<QuerySet [<MediaType: MediaType object (1)>]>
>>> Track.objects.aggregate(Max('unit_price')).filter(media_type = 1)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'filter'
>>> Track.objects.filter(media_type = 1)(.aggregate(Max('unit_price')).filter(media_type = 1)
  File "<console>", line 1
    Track.objects.filter(media_type = 1)(.aggregate(Max('unit_price')).filter(media_type = 1)
                                         ^
SyntaxError: invalid syntax
>>> Track.objects.filter(media_type = 1).aggregate(Max('unit_price')).filter(media_type = 1)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'filter'
>>> Track.objects.filter(media_type = 1).aggregate(Max('unit_price'))
{'unit_price__max': Decimal('0.99')}
>>> Track.objects.filter(media_type = 1).aggregate(Max('unit_price')).filter(media_type = 1)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'filter'
>>> Track.objects.filter(media_type = 1).aggregate(Max('unit_price'))
{'unit_price__max': Decimal('0.99')}
>>> Track.objects.title.filter(media_type = 1).aggregate(Max('unit_price'))
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Manager' object has no attribute 'title'
>>> track = Track.objects.filter(media_type = 1).aggregate(Max('unit_price'))
>>> track.name
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'name'
>>> Track.objects.filter(unti_price = 0.99)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/query.py", line 892, in filter
    return self._filter_or_exclude(False, *args, **kwargs)
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/query.py", line 910, in _filter_or_exclude
    clone.query.add_q(Q(*args, **kwargs))
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1290, in add_q
    clause, _ = self._add_q(q_object, self.used_aliases)
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1318, in _add_q
    split_subq=split_subq, simple_col=simple_col,
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1190, in build_filter
    lookups, parts, reffed_expression = self.solve_lookup_type(arg)
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1049, in solve_lookup_type
    _, field, _, lookup_parts = self.names_to_path(lookup_splitted, self.get_meta())
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1420, in names_to_path
    "Choices are: %s" % (name, ", ".join(available)))
django.core.exceptions.FieldError: Cannot resolve keyword 'unti_price' into field. Choices are: album, album_id, bytes, composer, created_at, genre, genre_id, id, media_type, media_type_id, milliseconds, name, playlists, unit_price, updated_at
>>> Track.objects.filter(unit_price = 0.99)
<QuerySet [<Track: Track object (4)>, <Track: Track object (5)>, <Track: Track object (6)>, <Track: Track object (7)>, <Track: Track object (8)>, <Track: Track object (9)>, <Track: Track object (10)>, <Track: Track object (11)>, <Track: Track object (12)>, <Track: Track object (13)>, <Track: Track object (14)>, <Track: Track object (15)>, <Track: Track object (16)>, <Track: Track object (17)>, <Track: Track object (18)>, <Track: Track object (20)>, <Track: Track object (21)>, <Track: Track object (22)>, <Track: Track object (23)>, <Track: Track object (24)>, '...(remaining elements truncated)...']>
>>> track = Track.objects.filter(media_type = 1).aggregate(Max('unit_price'))
>>> Track.objects.title.filter(media_type = 1).aggregate(Max('unit_price'))
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Manager' object has no attribute 'title'
>>> track = Track.objects.filter(media_type = 1).aggregate(Max('unit_price'))
>>> Track.objects.filter(media_type = 1).aggregate(Max('unit_price'))
{'unit_price__max': Decimal('0.99')}
>>> Track.objects.filter(unti_price = 0.99).filter(media_type = 1)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/query.py", line 892, in filter
    return self._filter_or_exclude(False, *args, **kwargs)
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/query.py", line 910, in _filter_or_exclude
    clone.query.add_q(Q(*args, **kwargs))
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1290, in add_q
    clause, _ = self._add_q(q_object, self.used_aliases)
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1318, in _add_q
    split_subq=split_subq, simple_col=simple_col,
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1190, in build_filter
    lookups, parts, reffed_expression = self.solve_lookup_type(arg)
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1049, in solve_lookup_type
    _, field, _, lookup_parts = self.names_to_path(lookup_splitted, self.get_meta())
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1420, in names_to_path
    "Choices are: %s" % (name, ", ".join(available)))
django.core.exceptions.FieldError: Cannot resolve keyword 'unti_price' into field. Choices are: album, album_id, bytes, composer, created_at, genre, genre_id, id, media_type, media_type_id, milliseconds, name, playlists, unit_price, updated_at
>>> Track.objects.filter(untit_price = 0.99).filter(media_type = 1)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/query.py", line 892, in filter
    return self._filter_or_exclude(False, *args, **kwargs)
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/query.py", line 910, in _filter_or_exclude
    clone.query.add_q(Q(*args, **kwargs))
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1290, in add_q
    clause, _ = self._add_q(q_object, self.used_aliases)
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1318, in _add_q
    split_subq=split_subq, simple_col=simple_col,
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1190, in build_filter
    lookups, parts, reffed_expression = self.solve_lookup_type(arg)
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1049, in solve_lookup_type
    _, field, _, lookup_parts = self.names_to_path(lookup_splitted, self.get_meta())
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1420, in names_to_path
    "Choices are: %s" % (name, ", ".join(available)))
django.core.exceptions.FieldError: Cannot resolve keyword 'untit_price' into field. Choices are: album, album_id, bytes, composer, created_at, genre, genre_id, id, media_type, media_type_id, milliseconds, name, playlists, unit_price, updated_at
>>> Track.objects.filter(unit_price = 0.99).filter(media_type = 1)
<QuerySet [<Track: Track object (6)>, <Track: Track object (7)>, <Track: Track object (8)>, <Track: Track object (9)>, <Track: Track object (10)>, <Track: Track object (11)>, <Track: Track object (12)>, <Track: Track object (13)>, <Track: Track object (14)>, <Track: Track object (15)>, <Track: Track object (16)>, <Track: Track object (17)>, <Track: Track object (18)>, <Track: Track object (20)>, <Track: Track object (21)>, <Track: Track object (22)>, <Track: Track object (23)>, <Track: Track object (24)>, <Track: Track object (26)>, <Track: Track object (27)>, '...(remaining elements truncated)...']>
>>> Track.objects.order_by('price')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/query.py", line 250, in __repr__
    data = list(self[:REPR_OUTPUT_SIZE + 1])
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/query.py", line 274, in __iter__
    self._fetch_all()
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/query.py", line 1242, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/query.py", line 55, in __iter__
    results = compiler.execute_sql(chunked_fetch=self.chunked_fetch, chunk_size=self.chunk_size)
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/compiler.py", line 1087, in execute_sql
    sql, params = self.as_sql()
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/compiler.py", line 474, in as_sql
    extra_select, order_by, group_by = self.pre_sql_setup()
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/compiler.py", line 55, in pre_sql_setup
    order_by = self.get_order_by()
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/compiler.py", line 330, in get_order_by
    field, self.query.get_meta(), default_order=asc))
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/compiler.py", line 704, in find_ordering_name
    field, targets, alias, joins, path, opts, transform_function = self._setup_joins(pieces, opts, alias)
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/compiler.py", line 734, in _setup_joins
    field, targets, opts, joins, path, transform_function = self.query.setup_joins(pieces, opts, alias)
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1504, in setup_joins
    names[:pivot], opts, allow_many, fail_on_missing=True,
  File "/home/yjacobs/.pyenv/versions/chinook/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1420, in names_to_path
    "Choices are: %s" % (name, ", ".join(available)))
django.core.exceptions.FieldError: Cannot resolve keyword 'price' into field. Choices are: album, album_id, bytes, composer, created_at, genre, genre_id, id, media_type, media_type_id, milliseconds, name, playlists, unit_price, updated_at
>>> Track.objects.order_by('unit_price')
<QuerySet [<Track: Track object (5)>, <Track: Track object (6)>, <Track: Track object (7)>, <Track: Track object (8)>, <Track: Track object (9)>, <Track: Track object (10)>, <Track: Track object (11)>, <Track: Track object (12)>, <Track: Track object (13)>, <Track: Track object (14)>, <Track: Track object (15)>, <Track: Track object (16)>, <Track: Track object (17)>, <Track: Track object (18)>, <Track: Track object (20)>, <Track: Track object (21)>, <Track: Track object (22)>, <Track: Track object (23)>, <Track: Track object (24)>, <Track: Track object (26)>, '...(remaining elements truncated)...']>
>>> Track.objects.filter(media_type = 1).order_by('unit_price')
<QuerySet [<Track: Track object (7)>, <Track: Track object (8)>, <Track: Track object (9)>, <Track: Track object (10)>, <Track: Track object (11)>, <Track: Track object (12)>, <Track: Track object (13)>, <Track: Track object (14)>, <Track: Track object (15)>, <Track: Track object (16)>, <Track: Track object (17)>, <Track: Track object (18)>, <Track: Track object (20)>, <Track: Track object (21)>, <Track: Track object (22)>, <Track: Track object (23)>, <Track: Track object (24)>, <Track: Track object (26)>, <Track: Track object (27)>, <Track: Track object (28)>, '...(remaining elements truncated)...']>
>>> Artist.objects.aggregate(Max('created_at'))
{'created_at__max': datetime.datetime(2014, 1, 17, 12, 58, 54, 378000, tzinfo=<UTC>)}
>>> Artist.objects.order_by('-created_at')
<QuerySet [<Artist: Artist object (187)>, <Artist: Artist object (41)>, <Artist: Artist object (189)>, <Artist: Artist object (87)>, <Artist: Artist object (1)>, <Artist: Artist object (150)>, <Artist: Artist object (75)>, <Artist: Artist object (98)>, <Artist: Artist object (149)>, <Artist: Artist object (93)>, <Artist: Artist object (165)>, <Artist: Artist object (9)>, <Artist: Artist object (264)>, <Artist: Artist object (35)>, <Artist: Artist object (131)>, <Artist: Artist object (117)>, <Artist: Artist object (105)>, <Artist: Artist object (260)>, <Artist: Artist object (231)>, <Artist: Artist object (129)>, '...(remaining elements truncated)...']>
>>> Artist.objects.get(name)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'name' is not defined
>>> Artist.objects.name
'objects'
>>> Artist.objects.get(pk = 187).name
'Los Hermanos'
>>> Artist.objects.get(pk = 41).name
'Elis Regina'
>>> Genre.objects.filter(name= 'Electronica/Dance')
<QuerySet [<Genre: Genre object (15)>]>
>>> Track.objects.title.filter(genre = 1).aggregate(Min('unit_price'))
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Manager' object has no attribute 'title'
>>> Track.objects.filter(genre = 1).aggregate(Min('unit_price'))
{'unit_price__min': Decimal('0.99')}
>>> Track.objects.filter(genre = 15).aggregate(Min('unit_price'))
{'unit_price__min': Decimal('0.99')}
>>> Track.objects.aggregate(Min('unit_price'))
{'unit_price__min': Decimal('0.99')}
>>> Track.objects.aggregate(Max('unit_price'))
{'unit_price__max': Decimal('1.99')}
>>> Track.objects.filter(media_type = 1).filter(genre = 15)
<QuerySet [<Track: Track object (3319)>, <Track: Track object (3320)>, <Track: Track object (3321)>, <Track: Track object (3322)>, <Track: Track object (3323)>, <Track: Track object (3324)>, <Track: Track object (3325)>, <Track: Track object (3327)>, <Track: Track object (3328)>, <Track: Track object (3329)>, <Track: Track object (3330)>, <Track: Track object (3331)>, <Track: Track object (3333)>, <Track: Track object (3334)>, <Track: Track object (3335)>, <Track: Track object (1456)>, <Track: Track object (1463)>, <Track: Track object (1455)>, <Track: Track object (3326)>, <Track: Track object (3332)>, '...(remaining elements truncated)...']>
>>> Track.objects.filter(media_type = 1).filter(genre = 15)
<QuerySet [<Track: Track object (3319)>, <Track: Track object (3320)>, <Track: Track object (3321)>, <Track: Track object (3322)>, <Track: Track object (3323)>, <Track: Track object (3324)>, <Track: Track object (3325)>, <Track: Track object (3327)>, <Track: Track object (3328)>, <Track: Track object (3329)>, <Track: Track object (3330)>, <Track: Track object (3331)>, <Track: Track object (3333)>, <Track: Track object (3334)>, <Track: Track object (3335)>, <Track: Track object (1456)>, <Track: Track object (1463)>, <Track: Track object (1455)>, <Track: Track object (3326)>, <Track: Track object (3332)>, '...(remaining elements truncated)...']>
