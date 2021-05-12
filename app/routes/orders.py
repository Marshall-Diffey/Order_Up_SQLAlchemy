from flask import Blueprint

bp = Blueprint("orders", __name__, url_prefix="")
# print(__name__)


@bp.route("/")
def index():
    return "Order Up!"
