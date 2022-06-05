from orator.migrations import Migration


class ChangePhoneNumberLength(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('users') as table:
            pass

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('users') as table:
            pass
