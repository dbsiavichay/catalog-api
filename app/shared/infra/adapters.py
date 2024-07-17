import logging

from botocore.exceptions import NoCredentialsError, PartialCredentialsError

from app.shared.domain.entities import Email
from app.shared.domain.ports import EmailPort

logger = logging.getLogger(__name__)


class SESEmailAdapter(EmailPort):
    def __init__(self, ses_client) -> None:
        self.ses_client = ses_client

    def send_email(self, email: Email):
        try:
            response = self.ses_client.send_email(
                Source=email.sender,
                Destination={
                    "ToAddresses": email.recipients,
                },
                Message={
                    "Subject": {"Data": email.subject, "Charset": "UTF-8"},
                    "Body": {
                        "Text": {"Data": email.body_text, "Charset": "UTF-8"},
                        "Html": {"Data": email.body_html, "Charset": "UTF-8"},
                    },
                },
            )
        except NoCredentialsError:
            logger.exception("Error: No se encontraron las credenciales de AWS.")
            return
        except PartialCredentialsError:
            logger.exception("Error: Las credenciales de AWS están incompletas.")
            return

        # Mostrar el ID del mensaje para confirmar el envío
        logger.info("Correo enviado! ID del mensaje:", response["MessageId"])
