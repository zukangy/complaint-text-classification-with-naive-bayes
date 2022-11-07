# Some utility functions
import pickle


def load_pickle(path: str):
    """
    Load a pickle object with given path
    :param path: path to the object
    :return: object
    """
    with open(path, 'rb') as f:
        object_ = pickle.load(f)
    return object_


def save_pickle(path: str, file_name: str, object_: object):
    """
    Save the object to the provided path as the provided name.
    :param path: path to save the object
    :param file_name: name of the object
    :param object_: the object
    :return: None
    """
    file_path = path + '/' + file_name + '.pkl'
    with open(file_path, 'wb') as f:
        pickle.dump(object_, f)
    print('The provided object has been saved to {} as {}'.format(path, file_name + '.pkl'))
    return