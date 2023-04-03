from django.shortcuts import render, redirect
from django.http import HttpResponse

from  .forms import NameForm

from pytube import YouTube
import os

from django.utils.encoding import smart_str

#def index(request):
    #return HttpResponse("Hello World.")

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #redirect to differnt view
            #return HttpResponseRedirect('/thanks/')
            print("hellofsdsfsdf")
            print(request.POST.get('url_link'))
            url = request.POST.get('url_link')
            yt = YouTube(url)
            videos = yt.streams.filter(only_audio=True).first()
            location='static/ytdl/audio/'
            out_file = videos.download(output_path=location)

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print("Sucessfull mp3 Dowmload!!")
            print("Sucessfull mp3 Dowmload!!")

            return redirect("list")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'main.html', {'form': form})

def url_link(request):
    return HttpResponse("Hello World.")



def list (request):
    #open audio file for reading
    #return file holder / stream
    audio_pointer = os.listdir('static/ytdl/audio/')

    audio_pointer = sorted(audio_pointer)
    print(audio_pointer)
    args = {}
    #make url array
    url = []
    pre_fix= 'static/ytdl/audio/'
    args ['audios'] = audio_pointer

    #RENAME all files
     #GET all the strings and take out all the spaces


    for audio in audio_pointer:
        #os.rename(audio, audio.replace(" ",""))
        print("begin----")
        loc = pre_fix + audio
        loc2 = pre_fix + audio.replace(" ","")
        os.rename(loc,loc2)
        print(loc)
        url.append(loc)
        print("end+++++++")
    args['urls'] = url
    print(url[0])

    return render(request, 'list.html', args )
    #put into array the mp3

    #send list to template
def download(request, pk):
    pre_fix= 'static/ytdl/audio/'
    audio_pointer = os.listdir('static/ytdl/audio/')
    audio_pointer = sorted(audio_pointer)

    print(pk)
    print(audio_pointer[int(pk)])
    sel =audio_pointer[int(pk)]
    url = pre_fix + sel
    print(url)

    with open (url,'rb') as filepath:
        response= HttpResponse(filepath.read() ,
        content_type = 'audio/mpeg')

        response['Content-Disposition'] = "attachment; filename={}".format(
        smart_str(sel))

        response['Content-Length'] = os.path.getsize(url)

        return response


#def download(request):
#    print("url_name")





# Create your views here.
