# Some utility functions
import pickle


def load_pickle(path):
    with open(path, 'rb') as f:
        object_ = pickle.load(f)
    return object_


def save_pickle(path, file_name, object_):
    file_path = path + '/' + file_name + '.pkl'
    with open(file_path, 'wb') as f:
        pickle.dump(object_, f)
    print('The provided object has been saved to {} as {}'.format(path, file_name + '.pkl'))