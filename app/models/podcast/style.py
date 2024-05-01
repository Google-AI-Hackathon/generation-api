from enum import Enum

class Style(str, Enum):
    conversational = 'conversational'
    structured = 'structured'
    narative = 'narative'
    debatable = 'debatable'
    educational = 'educational'
    entertaining = 'entertaining'