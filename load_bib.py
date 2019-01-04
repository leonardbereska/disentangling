import os.path as osp
import shutil
import requests
import subprocess

curdir = osp.abspath('.')

def add_dir(dir_name):
    curdir = osp.abspath('.')
    libpath = osp.join(curdir, dir_name)
    if not osp.exists(libpath):
        os.mkdir(libpath)
        print('made dir: {}'.format(dir_name))
    else:
        print('{} exists already'.format(dir_name))


def get_name(line):
    link_0 = line.find('{')
    link_1 = line.find(',')
    name = line[link_0+1:link_1]
    return name

def get_title(line):
    link_0 = line.find('}{')
    link_1 = line.find('}}')
    name = line[link_0+2:link_1]
    return name

def save_pdf(link, savename):
    print('access link: {}'.format(link))
    # r = requests.get(link, auth=('usrname', 'password'), verify=False,stream=True)
    # r.raw.decode_content = True
    # with open(savename, 'wb') as f:
        # shutil.copyfileobj(r.raw, f)

    # import urllib3
    # urllib3.disable_warnings()
    # with urllib3.PoolManager() as http:
        # r = http.request('GET', link)
        # with open(savename, 'wb') as fout:
            # fout.write(r.data)
    if osp.exists(savename):
        print('{} exists already'.format(savename))
    else:
        bashCommand = "curl -o {} {}".format(savename, link)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print('saved as {}'.format(savename))

def get_link(title):
    if title.find('\href')!=-1:
        link_0 = title.find('{')
        link_1 = title.find('}')
        link = title[link_0+7:link_1]  # 7 for deleting href
    else:
        link = None
    return link

def load_bib(bib_name):
    """read in bibtex file"""
    print("Reading BibTex File: {}".format(bib_name))
    curdir = osp.abspath('.')
    bib_path = osp.join(curdir, bib_name)
    print("Path: {}".format(bib_path))
    print('Creating library..')
    add_dir('library')
    with open(bib_path, 'r') as f:
        # txt = f.read()
        line = f.readline()
        i = 0
        start = False
        while line:
            i += 1
            if (line.find('@')==1) or start:  # reading entry
                if start == False:
                    filename = get_name(line)
                start = True
                if line.find('title')==1:
                    link = get_link(line)
                    if link is not None:
                        savepath = osp.join(curdir, 'library', filename+'.pdf')
                        save_pdf(link, savepath)
                if (line.find('}')==1):  # end of entry
                    start=False
            line = f.readline()
            print(i)  # print line number


def make_bib(bib_name, new_bib_name):
    """create bib file, replace internet links with local links"""
    print("Saving new Bib File..")
    """read in bibtex file"""
    print("Reading BibTex File: {}".format(bib_name))
    curdir = osp.abspath('.')
    bib_path = osp.join(curdir, bib_name)
    save_path = osp.join(curdir, new_bib_name)
    with open(bib_path, 'r') as f:
        with open(save_path, 'a') as f_new:
            line = f.readline()
            f_new.write(line)
            filename=None
            while line:
                if line.find('@')==1:  # reading entry
                    filename = get_name(line)
                if line.find('title')==1:
                    link = get_link(line)
                    new_link = osp.join('library', filename+'.pdf')
                    new_title = get_title(line)
                    new_title = '{'+new_title+'}'
                    new_link = '\href{run:'+new_link+'}'
                    new_title = new_link+new_title
                    new_title = '\ttitle={}'.format('{'+new_title+'},\n')
                    if link is not None:
                        line = new_title
                f_new.write(line)
                line = f.readline()
    print("Saved {}".format(new_bib_name))

def main():
    bib_name="lib.bib"
    new_bib_name="lib_new.bib"
    load_bib(bib_name)
    make_bib(bib_name, new_bib_name)

main()
