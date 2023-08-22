from auth.base_config import current_user
from fastapi import APIRouter, BackgroundTasks, Depends

from .tasks import send_email

router = APIRouter(prefix="/report")


@router.get("/dashboard")
def get_dashboard_report(background_tasks: BackgroundTasks, user=Depends(current_user)):
    send_email(user.username)
    background_tasks.add_task(send_email, user.username)
    send_email.delay(user.username)
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }
