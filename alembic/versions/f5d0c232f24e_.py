"""empty message

Revision ID: f5d0c232f24e
Revises: 
Create Date: 2019-01-11 00:44:31.207540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5d0c232f24e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    class_table = op.create_table('class',
    sa.Column('id', sa.String(length=500), nullable=False),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('class_leader', sa.String(length=500), nullable=True),
    sa.Column('created_on', sa.String(length=500), nullable=True),
    sa.Column('updated_on', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    student_table = op.create_table('student',
    sa.Column('id', sa.String(length=500), nullable=False),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('class_id', sa.String(length=500), nullable=True),
    sa.Column('created_on', sa.String(length=500), nullable=True),
    sa.Column('updated_on', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )

    op.bulk_insert(student_table,
                   [
                       {'id': 302196545109901605471370316978873835651, 'name': 'Ratan Boddu',
                        'class_id': 44426495382941689493289587869381099512, 'created_on': '01/03/19 07:45:54',
                        'updated_on': '01/03/19 07:45:54'},
                       {'id': 128133200461758240586121768451546423427, 'name': 'Sarvesh Deshmukh',
                        'class_id': 44426495382941689493289587869381099512, 'created_on': '01/03/19 07:45:54',
                        'updated_on': '01/03/19 07:45:54'},
                       {'id': 928133200461758240586121768451546423728, 'name': 'Shivani Singh',
                        'class_id': 44426495382941689493289587869381099512, 'created_on': '01/03/19 07:45:54',
                        'updated_on': '01/03/19 07:45:54'},
                       {'id': 728133200461758240586121768451546423028, 'name': 'Aditya Mane',
                        'class_id': 56426495382941689493289587869381088534, 'created_on': '01/03/19 07:45:54',
                        'updated_on': '01/03/19 07:45:54'},
                       {'id': 828133200461758240586121768451546423328, 'name': 'Aammir Shaikh',
                        'class_id': 56426495382941689493289587869381088534, 'created_on': '01/03/19 07:45:54',
                        'updated_on': '01/03/19 07:45:54'},
                       {'id': 311264963829416894932895872869381054595, 'name': 'Aayushi Agarwal',
                        'class_id': 56426495382941689493289587869381088534, 'created_on': '01/03/19 07:45:54',
                        'updated_on': '01/03/19 07:45:54'},
                       {'id': 31426495382941689493289587869381054503, 'name': 'Harsh Parikh',
                        'class_id': 62426495382941689493289587869381066556, 'created_on': '01/03/19 07:45:54',
                        'updated_on': '01/03/19 07:45:54'},
                       {'id': 52426495382941689493289587869381054503, 'name': 'Archit Masurkar',
                        'class_id': 62426495382941689493289587869381066556, 'created_on': '01/03/19 07:45:54',
                        'updated_on': '01/03/19 07:45:54'},
                       {'id': 81426495382941689493289587869381054503, 'name': 'Akshay Naik',
                        'class_id': 62426495382941689493289587869381066556, 'created_on': '01/03/19 07:45:54',
                        'updated_on': '01/03/19 07:45:54'},
                       {'id': 31426495382941689493289587869381054504, 'name': 'Rishi Kambil',
                        'class_id': 44426495382941689493289587869381099539, 'created_on': '01/03/19 07:45:54',
                        'updated_on': '01/03/19 07:45:54'},
                       {'id': 7426495382941689493289587869381054504, 'name': 'Pranjali Shirke',
                        'class_id': 44426495382941689493289587869381099539, 'created_on': '01/03/19 07:45:54',
                        'updated_on': '01/03/19 07:45:54'},
                       {'id': 31426495382941689493289587869381054999, 'name': 'Shalini Pereira',
                        'class_id': 44426495382941689493289587869381099539, 'created_on': '01/03/19 07:45:54',
                        'updated_on': '01/03/19 07:45:54'},
                   ]

                   )

    op.bulk_insert(class_table,
               [
                   {'id': 44426495382941689493289587869381099539, 'name': '10th A',
                    'class_leader': 31426495382941689493289587869381054504, 'created_on': '01/03/19 07:45:54',
                    'updated_on': '01/03/19 07:45:54'},
                   {'id': 44426495382941689493289587869381099512, 'name': '10th B',
                    'class_leader': 302196545109901605471370316978873835651, 'created_on': '01/03/19 07:45:54',
                    'updated_on': '01/03/19 07:45:54'},
                   {'id': 56426495382941689493289587869381088534, 'name': '10th C',
                    'class_leader': 311264963829416894932895872869381054595, 'created_on': '01/03/19 07:45:54',
                    'updated_on': '01/03/19 07:45:54'},
                   {'id': 62426495382941689493289587869381066556, 'name': '10th D',
                    'class_leader': 31426495382941689493289587869381054503, 'created_on': '01/03/19 07:45:54',
                    'updated_on': '01/03/19 07:45:54'},
               ]

               )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    op.drop_table('class')
    # ### end Alembic commands ###
