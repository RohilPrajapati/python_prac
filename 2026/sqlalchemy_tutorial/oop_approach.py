import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, declarative_base, Mapped, mapped_column

db = sa.create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=db)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)
    username: Mapped[str]
    email: Mapped[str]

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"


def main() -> None:
    Base.metadata.create_all(db)
    user = User(username="Rohil", email="rohil@rohil.com")
    user2 = User(username="Ram", email="ram@ram.com")

    with Session() as session:
        session.add(user)
        session.add(user2)
        session.commit()

        print(session.query(User).all())


if __name__ == "__main__":
    main()
