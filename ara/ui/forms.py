#  Copyright (c) 2019 Red Hat, Inc.
#
#  This file is part of ARA Records Ansible.
#
#  ARA is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  ARA is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with ARA.  If not, see <http://www.gnu.org/licenses/>.

from django import forms

from ara.api import models


class PlaybookSearchForm(forms.Form):
    ansible_version = forms.CharField(label="Ansible version", max_length=255, required=False)
    controller = forms.CharField(label="Playbook controller", max_length=255, required=False)
    name = forms.CharField(label="Playbook name", max_length=255, required=False)
    path = forms.CharField(label="Playbook path", max_length=255, required=False)
    status = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=models.Playbook.STATUS, required=False
    )
    label = forms.CharField(label="Playbook label", max_length=255, required=False)
    started_after = forms.DateField(label="Started after", required=False)
    order = forms.CharField(label="Order", max_length=255, required=False)


class ResultSearchForm(forms.Form):
    host = forms.CharField(label="Host id", max_length=10, required=False)
    task = forms.CharField(label="Task id", max_length=10, required=False)
    changed = forms.BooleanField(label="Changed", required=False)

    status = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=models.Result.STATUS, required=False
    )
