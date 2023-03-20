from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect


# Permission Classes
from django.contrib.auth.mixins import LoginRequiredMixin
from visitor.permission import VisitorPassesTestMixin

# Django class based view
from django.views.generic import DetailView
from django.views.generic import UpdateView


# Models 
from accounts.models import Profile
from accounts.models import PresentAddress
from accounts.models import PermanentAddress
from visitor.models import VisitorInfo
from visitor.models import VisitorMediaLink

# Forms
from accounts.forms import ProfileForm
from accounts.forms import PresentAddressForm
from accounts.forms import PermanentAddressForm
from visitor.forms import VisitorInfoForm
from visitor.forms import VisitorMediaLinkForm



class VisitorProfileView(LoginRequiredMixin, VisitorPassesTestMixin, DetailView):
    queryset = Profile.objects.all()
    context_object_name = 'profile'
    template_name = 'visitor/profile.html'

    def test_func(self):
        return self.request.user.is_visitor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Profile Details'
        context["visitorinfo"] = VisitorInfo.objects.get(user=self.request.user)
        context["present_address"] = PresentAddress.objects.get(address_of=self.request.user)
        context["permanent_address"] = PermanentAddress.objects.get(address_of=self.request.user)
        context["media_link"] = VisitorMediaLink.objects.get(link_of=self.request.user)
         
        return context
    

class EditProfileView(LoginRequiredMixin, VisitorPassesTestMixin, UpdateView):
    model = Profile
    model2 = VisitorInfo
    form_class = ProfileForm
    form_class2 = VisitorInfoForm
    template_name = 'visitor/edit_profile.html'
    success_url = reverse_lazy('visitor:visitor_home')

    def test_func(self):
        return self.request.user.is_visitor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Add/Edit Profile'
        context["form"] = self.form_class(instance=self.request.user.profile) 
        context["info_form"] = self.form_class2(instance=self.request.user.visitor_info) 
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES, instance=self.request.user.profile)
        form2 = self.form_class2(request.POST, instance=self.request.user.visitor_info)
        return self.form_valid(form, form2)
    
    def form_valid(self, form, form2):
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.success(self.request, "Profile Updated Successfully")
        return super().form_valid(form,)
    

class EditAddressView(LoginRequiredMixin, VisitorPassesTestMixin, UpdateView):
    model = PresentAddress
    model2 = PermanentAddress
    form_class = PresentAddressForm
    form_class2 = PermanentAddressForm
    template_name = 'visitor/add_address.html'
    success_url = reverse_lazy('visitor:visitor_home')

    def test_func(self):
        return self.request.user.is_visitor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add/Edit Address"
        context["present_address"] = self.form_class(instance=self.request.user.present_address)
        context["permanent_address"] = self.form_class2(instance=self.request.user.permanent_address)
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.request.user.present_address)
        form2 = self.form_class2(request.POST, instance=self.request.user.permanent_address)
        
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.success(self.request, "Add/Update Address Successfully")
            return HttpResponseRedirect("/profile/"+str(request.user.profile.id))
        else:
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Some thing went wrong try again")
        return super().form_invalid(form)

class UpdateMediaLinkView(LoginRequiredMixin, VisitorPassesTestMixin, UpdateView):
    model = VisitorMediaLink
    form_class = VisitorMediaLinkForm
    template_name = 'visitor/edit_media_link.html'
    success_url = reverse_lazy('visitor:visitor_home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add/Update Profile Media Link" 
        return context

    def form_valid(self, form):
        messages.success(self.request, "Visitor Medial Link Added/Update Successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Some thing wrong try again")
        return super().form_invalid(form)
    