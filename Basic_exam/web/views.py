from django.shortcuts import render, redirect

from Basic_exam.web.forms import CreateProfile, DeleteProfile, AddAlbum, EdieAlbum, DeleteAlbum
from Basic_exam.web.models import Profile, Album


def get_profile():
    current_profile = Profile.objects.all()
    if current_profile:
        return current_profile[0]
    return None


def action_create_form(request, current_form, current_redirect, current_template):
    if request.method == 'POST':
        form = current_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(current_redirect)
    form = current_form()
    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, current_template, context)


def action_edit_form(request, current_form, current_redirect, current_template, instance):
    if request.method == 'POST':
        form = current_form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(current_redirect)
    form = current_form(instance=instance)
    context = {
        'form': form,
        'pk': instance,
    }
    return render(request, current_template, context)


def home(request):
    profile = get_profile()
    albums = Album.objects.all()
    if not profile:
        return redirect('create profile')
    context = {
        'albums': albums,
        'profile': profile,
    }
    return render(request, 'home-with-profile.html', context)


def add_album(request):
    return action_create_form(request, AddAlbum, 'home', 'add-album.html')


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album,
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    return action_edit_form(request, EdieAlbum, 'home', 'edit-album.html', Album.objects.get(pk=pk))


def delete_album(request, pk):
    return action_edit_form(request, DeleteAlbum, 'home', 'delete-album.html', Album.objects.get(pk=pk))


def create_profile(request):
    return action_create_form(request, CreateProfile, 'home', 'home-no-profile.html')


def profile_details(request):
    albums = Album.objects.all()
    current_profile = get_profile()
    context = {
        'current_profile': current_profile,
        'count_albums': len(albums),
    }
    return render(request, 'profile-details.html', context)


def delete_profile(request):
    Album.objects.all().delete()
    return action_edit_form(request, DeleteProfile, 'create profile', 'profile-delete.html', get_profile())

