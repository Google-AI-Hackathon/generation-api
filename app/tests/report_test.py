from app.utils.record import load_conversation_interactions, save_report
from app.services.summary_service import generate_report

title = 'brainstorming'
report = generate_report(load_conversation_interactions(title))
save_report(report, title)