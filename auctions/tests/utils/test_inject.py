import abc
import inject

class Cache(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def save(self, value, object):
        pass

class RedisCache(Cache):
    def __init__(self, config):
        self.config = config

    def save(self, key, value):
        print(f'{key}:{value}')


# `inject.instance` requests dependencies from the injector.
def foo(bar):
    cache = inject.instance(Cache)
    cache.save('bar', bar)



# Create an optional configuration.
def application_config(binder):
    binder.bind(Cache, RedisCache('localhost:1234'))

inject.configure(application_config)


foo('Hello')

# # `inject.params` injects dependencies as keyword arguments or positional argument. 
# # Also you can use @inject.autoparams in Python 3.5, see the example above.
# @inject.params(cache=Cache, user=CurrentUser)
# def baz(foo, cache=None, user=None):
#     cache.save('foo', foo, user)

# # this can be called in different ways:
# # with injected arguments
# baz('foo')

# # with positional arguments
# baz('foo', my_cache)

# # with keyword arguments
# baz('foo', my_cache, user=current_user)


# # `inject.param` is deprecated, use `inject.params` instead.
# @inject.param('cache', Cache)
# def bar(foo, cache=None):
#     cache.save('foo', foo)


# # `inject.attr` creates properties (descriptors) which request dependencies on access.
# class User(object):
#     cache = inject.attr(Cache)
#     def __init__(self, id):
#         self.id = id

#     def save(self):
#         self.cache.save('users', self)

#     @classmethod
#     def load(cls, id):
#         return cls.cache.load('users', id)


# # Create an optional configuration.
# def my_config(binder):
#     binder.install(my_config2)  # Add bindings from another config.
#     binder.bind(Cache, RedisCache('localhost:1234'))

# # Configure a shared injector.
# inject.configure(my_config)


# # Instantiate User as a normal class. Its `cache` dependency is injected when accessed.
# user = User(10)
# user.save()

# # Call the functions, the dependencies are automatically injected.
# foo('Hello')
# bar('world')