#!/usr/bin/env python3
#-*- coding: utf-8 -*-


"""
Module with event support implementation
"""

from __future__ import annotations


class ObjectWithEvents:

    callbacks: dict[str, list[object]] = None

    def addEvent(self, eventname, callback):
        """
        Adds new callback to a given event
        or if none creates new event
        """
        if self.callbacks is None:
            self.callbacks = {}
        if eventname not in self.callbacks:
            self.callbacks[eventname] = [callback]
        else:
            self.callbacks[eventname].append(callback)

    def delEvent(self, eventname, callback):
        """
        Deletes callback from a given event
        """
        if self.callbacks is not None and eventname in self.callbacks:
            if callback in self.callbacks[eventname]:
                self.callbacks[eventname].remove(callback)

    def triggerEvent(self, eventname):
        """
        Triggers all callbacks of a given event
        """
        if self.callbacks is not None and eventname in self.callbacks:
            for callback in self.callbacks[eventname]:
                callback()

