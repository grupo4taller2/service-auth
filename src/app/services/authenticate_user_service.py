from src.app.ports.inbound.authenticate_user_usecase \
    import AuthenticateUserUseCase, AuthenticateUserCommand

from src.app.domain.credentials import Credentials

from src.app.ports.outbound.load_user_port import LoadUserPort


class AuthenticateUserService(AuthenticateUserUseCase):
    def authenticateUser(command: AuthenticateUserCommand):
        # TODO: Here goes logic
        # LoadUserPortConcreto para reconstruir Users con repositories
        credentials = Credentials(command.email, command.password)
        
