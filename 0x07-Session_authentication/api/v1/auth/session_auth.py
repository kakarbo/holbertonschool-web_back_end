#!/usr/bin/env python3
"""Module of class auth"""
from api.v1.auth.auth import Auth
import uuid
from models.base import Base


class SessionAuth(Auth):
    """class SessionAuth
    """
    user_id_by_session_id = dict()

    def create_session(self, user_id: str = None) -> str:
        """instance method create_session
        """
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """instance method user_id_for_session_id
        """
        if session_id is None:
            return None
        if type(session_id) is not str:
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        self.user_id_by_session_id[session_id] = user_id

        return user_id