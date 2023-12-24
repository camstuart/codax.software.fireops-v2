from piccolo.table import Table
import piccolo.columns as col
from datetime import datetime, timezone


class User(Table, tablename="users"):
    """
    Users that have registered via oAuth/OIDC
    """

    id = col.UUID(primary_key=True)
    name = col.Varchar(required=True, length=200)
    email = col.Varchar(required=True, Unique=True, length=200)
    image = col.Varchar(required=False, length=500)
    active = col.Boolean(default=True)
    created_dt = col.Timestamptz(default=datetime.now)
    updated_dt = col.Timestamptz(default=datetime.now, auto_update=datetime.now)


class Account(Table, tablename="accounts"):
    """
    Account providers
    """

    id = col.UUID(primary_key=True)
    user = col.ForeignKey(references=User)
    type = col.Varchar(required=True, length=50)
    provider = col.Varchar(required=True, length=100)
    providerAccountId = col.Varchar(length=100)
    created_dt = col.Timestamptz(default=datetime.now)
    updated_dt = col.Timestamptz(default=datetime.now, auto_update=datetime.now)


class VerificationToken(Table, tablename="verification_tokens"):
    """
    User Account Verification Tokens
    """

    id = col.UUID(primary_key=True)
    user = col.ForeignKey(references=User)
    identifier = col.Varchar(required=True, length=200)
    token = col.Varchar(required=True, length=1000)
    expires = col.Timestamptz()
    created_dt = col.Timestamptz(default=datetime.now)
    updated_dt = col.Timestamptz(default=datetime.now, auto_update=datetime.now)
