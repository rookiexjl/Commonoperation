# coding:utf-8
import os


def dirlist(path, allfile):
    '''
        list all file
    '''
    try:
        filelist = os.listdir(path)
        for filename in filelist:
            filepath = os.path.join(path, filename)
            if os.path.isdir(filepath):
                dirlist(filepath, allfile)
            else:
                allfile.append(filepath)

        return allfile
    except WindowsError:
        print "WindowsError系统调用失败"
        pass
        


def npglist(allfile, ngplist):
    '''
        return .npg file
    '''
    for file in allfile:
        if file.endswith('.npg'):
            npglist.append(file)
    return npglist
    

if __name__ == '__main__':
    path = 'c:\\'
    allfile = dirlist(path, [])
    print len(allfile)
    npglist = npglist(allfile, [])
    print npglist
