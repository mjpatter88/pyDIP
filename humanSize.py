SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}


def approx_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human-readable form.'''
    if size < 0:
        raise ValueError('number must be positive')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000

    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)
    pass

def sys_test(module):
    print(module.path)

if __name__ == '__main__':
    print(approx_size(1000000000000, False))
    print(approx_size(1000000000000))
