import DbHelper

def singleton(_class):
    """
        a decorator that is used to implement singleton patten;
        Usage:
            @singleton
            class Foo:
                pass
    """
    instances = {}

    def _getInstance(*args, **kwargs):
        if _class not in instances:
            instances[_class] = _class(*args, **kwargs)
        return instances[_class]

    return _getInstance


def enum(*sequential):
    """
        pseudo Enum type;  Usage: EnumType=enum('key1','key2',...,)
    """
    enums = dict(zip(sequential, range(len(sequential))))
    return type('Enum', (), enums)


def checkDB(fun):
    def _fun(self, *args):
        if self.db is None:
            self.db = DbHelper.DbHelper()
        fun(self, *args)
    return _fun