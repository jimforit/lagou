#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'jimit'
__CreateAt__ = '2019\3\7 15:28'

from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initialkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initialkwargs)
        return login_required(view)