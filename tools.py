import configparser

headers = {
    'Content-Type': 'application/json',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
}


def get_config(filepath: str) -> dict:
    """
    读取账号配置信息
    :param filepath: 文件路径
    """
    config = configparser.ConfigParser()
    config.read(filepath, encoding='utf-8-sig')
    items = config._sections
    items = dict(items)
    for item in items:
        items[item] = dict(items[item])
    return items
