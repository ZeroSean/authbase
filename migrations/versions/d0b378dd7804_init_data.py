"""init data

Revision ID: d0b378dd7804
Revises: None
Create Date: 2017-06-25 09:38:48.564000

"""

# revision identifiers, used by Alembic.
revision = 'd0b378dd7804'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('SYONLINE',
    sa.Column('ID', sa.String(length=36), nullable=False),
    sa.Column('CREATEDATETIME', sa.DateTime(), nullable=True),
    sa.Column('LOGINNAME', sa.String(length=100), nullable=True),
    sa.Column('IP', sa.String(length=100), nullable=True),
    sa.Column('TYPE', sa.String(length=1), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_SYONLINE_CREATEDATETIME'), 'SYONLINE', ['CREATEDATETIME'], unique=False)
    op.create_table('SYORGANIZATION',
    sa.Column('ID', sa.String(length=36), nullable=False),
    sa.Column('CREATEDATETIME', sa.DateTime(), nullable=True),
    sa.Column('UPDATEDATETIME', sa.DateTime(), nullable=True),
    sa.Column('NAME', sa.String(length=200), nullable=True),
    sa.Column('ADDRESS', sa.String(length=200), nullable=True),
    sa.Column('CODE', sa.String(length=200), nullable=True),
    sa.Column('ICONCLS', sa.String(length=100), nullable=True),
    sa.Column('SEQ', sa.Integer(), nullable=True),
    sa.Column('SYORGANIZATION_ID', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['SYORGANIZATION_ID'], ['SYORGANIZATION.ID'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_SYORGANIZATION_CREATEDATETIME'), 'SYORGANIZATION', ['CREATEDATETIME'], unique=False)
    op.create_index(op.f('ix_SYORGANIZATION_UPDATEDATETIME'), 'SYORGANIZATION', ['UPDATEDATETIME'], unique=False)
    op.create_table('SYRESOURCETYPE',
    sa.Column('ID', sa.String(length=36), nullable=False),
    sa.Column('CREATEDATETIME', sa.DateTime(), nullable=True),
    sa.Column('UPDATEDATETIME', sa.DateTime(), nullable=True),
    sa.Column('NAME', sa.String(length=100), nullable=True),
    sa.Column('DESCRIPTION', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_SYRESOURCETYPE_CREATEDATETIME'), 'SYRESOURCETYPE', ['CREATEDATETIME'], unique=False)
    op.create_index(op.f('ix_SYRESOURCETYPE_UPDATEDATETIME'), 'SYRESOURCETYPE', ['UPDATEDATETIME'], unique=False)
    op.create_table('SYROLE',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('CREATEDATETIME', sa.DateTime(), nullable=True),
    sa.Column('UPDATEDATETIME', sa.DateTime(), nullable=True),
    sa.Column('NAME', sa.String(length=100), nullable=True),
    sa.Column('DESCRIPTION', sa.String(length=200), nullable=True),
    sa.Column('ICONCLS', sa.String(length=100), nullable=True),
    sa.Column('SEQ', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_SYROLE_CREATEDATETIME'), 'SYROLE', ['CREATEDATETIME'], unique=False)
    op.create_index(op.f('ix_SYROLE_UPDATEDATETIME'), 'SYROLE', ['UPDATEDATETIME'], unique=False)
    op.create_table('SYUSER',
    sa.Column('ID', sa.String(length=36), nullable=False),
    sa.Column('CREATEDATETIME', sa.DateTime(), nullable=True),
    sa.Column('UPDATEDATETIME', sa.DateTime(), nullable=True),
    sa.Column('LOGINNAME', sa.String(length=100), nullable=True),
    sa.Column('PWD', sa.String(length=100), nullable=True),
    sa.Column('NAME', sa.String(length=100), nullable=True),
    sa.Column('SEX', sa.String(length=1), nullable=True),
    sa.Column('AGE', sa.Integer(), nullable=True),
    sa.Column('PHOTO', sa.String(length=200), nullable=True),
    sa.Column('EMPLOYDATE', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_SYUSER_CREATEDATETIME'), 'SYUSER', ['CREATEDATETIME'], unique=False)
    op.create_index(op.f('ix_SYUSER_LOGINNAME'), 'SYUSER', ['LOGINNAME'], unique=True)
    op.create_index(op.f('ix_SYUSER_UPDATEDATETIME'), 'SYUSER', ['UPDATEDATETIME'], unique=False)
    op.create_table('SYRESOURCE',
    sa.Column('ID', sa.String(length=36), nullable=False),
    sa.Column('CREATEDATETIME', sa.DateTime(), nullable=True),
    sa.Column('UPDATEDATETIME', sa.DateTime(), nullable=True),
    sa.Column('NAME', sa.String(length=100), nullable=True),
    sa.Column('URL', sa.String(length=200), nullable=True),
    sa.Column('DESCRIPTION', sa.String(length=200), nullable=True),
    sa.Column('ICONCLS', sa.String(length=100), nullable=True),
    sa.Column('SEQ', sa.Integer(), nullable=True),
    sa.Column('TARGET', sa.String(length=100), nullable=True),
    sa.Column('SYRESOURCETYPE_ID', sa.String(), nullable=True),
    sa.Column('SYRESOURCE_ID', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['SYRESOURCETYPE_ID'], ['SYRESOURCETYPE.ID'], ),
    sa.ForeignKeyConstraint(['SYRESOURCE_ID'], ['SYRESOURCE.ID'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_SYRESOURCE_CREATEDATETIME'), 'SYRESOURCE', ['CREATEDATETIME'], unique=False)
    op.create_index(op.f('ix_SYRESOURCE_UPDATEDATETIME'), 'SYRESOURCE', ['UPDATEDATETIME'], unique=False)
    op.create_table('SYUSER_SYORGANIZATION',
    sa.Column('SYUSER_ID', sa.String(), nullable=True),
    sa.Column('SYORGANIZATION_ID', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['SYORGANIZATION_ID'], ['SYORGANIZATION.ID'], ),
    sa.ForeignKeyConstraint(['SYUSER_ID'], ['SYUSER.ID'], )
    )
    op.create_table('SYUSER_SYROLE',
    sa.Column('SYUSER_ID', sa.String(), nullable=True),
    sa.Column('SYROLE_ID', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['SYROLE_ID'], ['SYROLE.ID'], ),
    sa.ForeignKeyConstraint(['SYUSER_ID'], ['SYUSER.ID'], )
    )
    op.create_table('SYORGANIZATION_SYRESOURCE',
    sa.Column('SYRESOURCE_ID', sa.String(), nullable=True),
    sa.Column('SYORGANIZATION_ID', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['SYORGANIZATION_ID'], ['SYORGANIZATION.ID'], ),
    sa.ForeignKeyConstraint(['SYRESOURCE_ID'], ['SYRESOURCE.ID'], )
    )
    op.create_table('SYROLE_SYRESOURCE',
    sa.Column('SYROLE_ID', sa.String(), nullable=True),
    sa.Column('SYRESOURCE_ID', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['SYRESOURCE_ID'], ['SYRESOURCE.ID'], ),
    sa.ForeignKeyConstraint(['SYROLE_ID'], ['SYROLE.ID'], )
    )
    op.drop_table('syrole_syresource')
    op.drop_table('t_base_pinyin')
    op.drop_table('syresource')
    op.drop_table('syappversiontype')
    op.drop_table('syresourcetype')
    op.drop_table('syappversiondetail')
    op.drop_table('syorganization_syresource')
    op.drop_table('syiosappversiondetail')
    op.drop_table('syonline')
    op.drop_table('syuser')
    op.drop_table('syostype')
    op.drop_table('syorganization')
    op.drop_table('syrole')
    op.drop_table('syuser_syorganization')
    op.drop_table('syuser_syrole')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('syuser_syrole',
    sa.Column('SYUSER_ID', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('SYROLE_ID', mysql.VARCHAR(length=36), nullable=False),
    sa.ForeignKeyConstraint(['SYROLE_ID'], [u'syrole.ID'], name=u'FK_j7iwtgslc2esrjx0ptieleoko'),
    sa.ForeignKeyConstraint(['SYUSER_ID'], [u'syuser.ID'], name=u'FK_1pi4p5h4y5ghbs5f4gdlgn620'),
    sa.PrimaryKeyConstraint('SYROLE_ID', 'SYUSER_ID'),
    mysql_default_charset=u'gbk',
    mysql_engine=u'InnoDB'
    )
    op.create_table('syuser_syorganization',
    sa.Column('SYUSER_ID', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('SYORGANIZATION_ID', mysql.VARCHAR(length=36), nullable=False),
    sa.ForeignKeyConstraint(['SYORGANIZATION_ID'], [u'syorganization.ID'], name=u'FK_14ewqc5wtscac0dd5rswrm5j2'),
    sa.ForeignKeyConstraint(['SYUSER_ID'], [u'syuser.ID'], name=u'FK_63bdmtxwlk259id13rp4iryy'),
    sa.PrimaryKeyConstraint('SYORGANIZATION_ID', 'SYUSER_ID'),
    mysql_default_charset=u'gbk',
    mysql_engine=u'InnoDB'
    )
    op.create_table('syrole',
    sa.Column('ID', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('CREATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.Column('DESCRIPTION', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('ICONCLS', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('NAME', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('SEQ', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('UPDATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('ID'),
    mysql_default_charset=u'gbk',
    mysql_engine=u'InnoDB'
    )
    op.create_table('syorganization',
    sa.Column('ID', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('ADDRESS', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('CODE', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('CREATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.Column('ICONCLS', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('NAME', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('SEQ', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('UPDATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.Column('SYORGANIZATION_ID', mysql.VARCHAR(length=36), nullable=True),
    sa.ForeignKeyConstraint(['SYORGANIZATION_ID'], [u'syorganization.ID'], name=u'FK_acf7qlb04quthktalwx8c7q69'),
    sa.PrimaryKeyConstraint('ID'),
    mysql_default_charset=u'gbk',
    mysql_engine=u'InnoDB'
    )
    op.create_table('syostype',
    sa.Column('ID', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('CREATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.Column('DESCRIPTION', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('NAME', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('UPDATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('ID'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('syuser',
    sa.Column('ID', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('AGE', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('CREATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.Column('LOGINNAME', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('NAME', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('PHOTO', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('PWD', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('SEX', mysql.VARCHAR(length=1), nullable=True),
    sa.Column('UPDATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.Column('EMPLOYDATE', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('ID'),
    mysql_default_charset=u'gbk',
    mysql_engine=u'InnoDB'
    )
    op.create_table('syonline',
    sa.Column('ID', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('CREATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.Column('IP', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('LOGINNAME', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('TYPE', mysql.VARCHAR(length=1), nullable=True),
    sa.PrimaryKeyConstraint('ID'),
    mysql_default_charset=u'gbk',
    mysql_engine=u'InnoDB'
    )
    op.create_table('syiosappversiondetail',
    sa.Column('ID', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('BUNDLEIDENTIFIER', mysql.LONGTEXT(), nullable=True),
    sa.Column('BUNDLEVERSION', mysql.LONGTEXT(), nullable=True),
    sa.Column('CREATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.Column('DESCRIPTION', mysql.LONGTEXT(), nullable=True),
    sa.Column('DISPLAYIMAGE', mysql.LONGTEXT(), nullable=True),
    sa.Column('FULLSIZEIMAGE', mysql.LONGTEXT(), nullable=True),
    sa.Column('MANIFEST', mysql.LONGTEXT(), nullable=True),
    sa.Column('PATH', mysql.LONGTEXT(), nullable=True),
    sa.Column('UPDATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.Column('APP_VERSION_TYPE_ID', mysql.VARCHAR(length=36), nullable=True),
    sa.ForeignKeyConstraint(['APP_VERSION_TYPE_ID'], [u'syappversiontype.ID'], name=u'FK_hxu1shhn595b10086i87i2ugy'),
    sa.PrimaryKeyConstraint('ID'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('syorganization_syresource',
    sa.Column('SYRESOURCE_ID', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('SYORGANIZATION_ID', mysql.VARCHAR(length=36), nullable=False),
    sa.ForeignKeyConstraint(['SYORGANIZATION_ID'], [u'syorganization.ID'], name=u'FK_acpjp8a7fjo0cnn02eb0ia6uf'),
    sa.ForeignKeyConstraint(['SYRESOURCE_ID'], [u'syresource.ID'], name=u'FK_m4mfglk7odi78d8pk9pif44vc'),
    sa.PrimaryKeyConstraint('SYORGANIZATION_ID', 'SYRESOURCE_ID'),
    mysql_default_charset=u'gbk',
    mysql_engine=u'InnoDB'
    )
    op.create_table('syappversiondetail',
    sa.Column('ID', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('CREATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.Column('DESCRIPTION', mysql.LONGTEXT(), nullable=True),
    sa.Column('PATH', mysql.LONGTEXT(), nullable=True),
    sa.Column('UPDATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.Column('VERSIONNUMBER', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('APP_VERSION_TYPE_ID', mysql.VARCHAR(length=36), nullable=True),
    sa.Column('VERSIONCODE', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['APP_VERSION_TYPE_ID'], [u'syappversiontype.ID'], name=u'FK_jvwredth6cc5loclls93eogk3'),
    sa.PrimaryKeyConstraint('ID'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('syresourcetype',
    sa.Column('ID', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('CREATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.Column('DESCRIPTION', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('NAME', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('UPDATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('ID'),
    mysql_default_charset=u'gbk',
    mysql_engine=u'InnoDB'
    )
    op.create_table('syappversiontype',
    sa.Column('ID', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('CREATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.Column('DESCRIPTION', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('NAME', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('UPDATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.Column('VERSIONFILEPATH', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('ID'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('syresource',
    sa.Column('ID', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('CREATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.Column('DESCRIPTION', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('ICONCLS', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('NAME', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('SEQ', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('TARGET', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('UPDATEDATETIME', mysql.DATETIME(), nullable=True),
    sa.Column('URL', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('SYRESOURCE_ID', mysql.VARCHAR(length=36), nullable=True),
    sa.Column('SYRESOURCETYPE_ID', mysql.VARCHAR(length=36), nullable=True),
    sa.ForeignKeyConstraint(['SYRESOURCETYPE_ID'], [u'syresourcetype.ID'], name=u'FK_93qfpiiuk3rwb32gc5mcmmlgh'),
    sa.ForeignKeyConstraint(['SYRESOURCE_ID'], [u'syresource.ID'], name=u'FK_n8kk2inhw4y4gax3nra2etfup'),
    sa.PrimaryKeyConstraint('ID'),
    mysql_default_charset=u'gbk',
    mysql_engine=u'InnoDB'
    )
    op.create_table('t_base_pinyin',
    sa.Column('pin_yin_', mysql.VARCHAR(charset=u'gbk', length=255), nullable=False),
    sa.Column('code_', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('code_'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('syrole_syresource',
    sa.Column('SYROLE_ID', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('SYRESOURCE_ID', mysql.VARCHAR(length=36), nullable=False),
    sa.ForeignKeyConstraint(['SYRESOURCE_ID'], [u'syresource.ID'], name=u'FK_kkrartsovl2frhfvriqdi7jwl'),
    sa.ForeignKeyConstraint(['SYROLE_ID'], [u'syrole.ID'], name=u'FK_r139h669pg4ts6mbvn3ip5472'),
    sa.PrimaryKeyConstraint('SYRESOURCE_ID', 'SYROLE_ID'),
    mysql_default_charset=u'gbk',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('SYROLE_SYRESOURCE')
    op.drop_table('SYORGANIZATION_SYRESOURCE')
    op.drop_table('SYUSER_SYROLE')
    op.drop_table('SYUSER_SYORGANIZATION')
    op.drop_index(op.f('ix_SYRESOURCE_UPDATEDATETIME'), table_name='SYRESOURCE')
    op.drop_index(op.f('ix_SYRESOURCE_CREATEDATETIME'), table_name='SYRESOURCE')
    op.drop_table('SYRESOURCE')
    op.drop_index(op.f('ix_SYUSER_UPDATEDATETIME'), table_name='SYUSER')
    op.drop_index(op.f('ix_SYUSER_LOGINNAME'), table_name='SYUSER')
    op.drop_index(op.f('ix_SYUSER_CREATEDATETIME'), table_name='SYUSER')
    op.drop_table('SYUSER')
    op.drop_index(op.f('ix_SYROLE_UPDATEDATETIME'), table_name='SYROLE')
    op.drop_index(op.f('ix_SYROLE_CREATEDATETIME'), table_name='SYROLE')
    op.drop_table('SYROLE')
    op.drop_index(op.f('ix_SYRESOURCETYPE_UPDATEDATETIME'), table_name='SYRESOURCETYPE')
    op.drop_index(op.f('ix_SYRESOURCETYPE_CREATEDATETIME'), table_name='SYRESOURCETYPE')
    op.drop_table('SYRESOURCETYPE')
    op.drop_index(op.f('ix_SYORGANIZATION_UPDATEDATETIME'), table_name='SYORGANIZATION')
    op.drop_index(op.f('ix_SYORGANIZATION_CREATEDATETIME'), table_name='SYORGANIZATION')
    op.drop_table('SYORGANIZATION')
    op.drop_index(op.f('ix_SYONLINE_CREATEDATETIME'), table_name='SYONLINE')
    op.drop_table('SYONLINE')
    # ### end Alembic commands ###
