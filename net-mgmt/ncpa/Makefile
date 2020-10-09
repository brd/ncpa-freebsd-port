# Created by: Brad Davis
# $FreeBSD: $

PORTNAME=	ncpa
PORTVERSION=	2.2.2
CATEGORIES=	net-mgmt

MAINTAINER=	brd@FreeBSD.org
COMMENT=	Nagios Cross-Platform Agent

USE_GITHUB=	yes
GH_ACCOUNT=	NagiosEnterprises
GH_TAGNAME=	5590da6

USES=		python:2.7 shebangfix
USE_RC_SUBR=	ncpa_listener ncpa_passive

NAGIOSUSER?=	nagios
NAGIOSGROUP?=	nagios
USERS=		${NAGIOSUSER}
GROUPS=		${NAGIOSGROUP}
LICENSE=	GPLv3

#BUILD_DEPENDS=	libffi>0:devel/libffi \
		${PYTHON_PKGNAMEPREFIX}appdirs>0:devel/py-appdirs@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}cffi>0:devel/py-cffi@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}cryptography>0:security/py-cryptography@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}docutils>0:textproc/py-docutils@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}Flask>0:www/py-flask@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}gevent-websocket>0:www/py-gevent-websocket@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}Jinja2>0:devel/py-Jinja2@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}kafka-python>0:net/py-kafka-python@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}openssl>0:security/py-openssl@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}packaging>0:devel/py-packaging@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}psutil>0:sysutils/py-psutil@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>0:www/py-requests@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}sqlite3>=2.7.8:databases/py-sqlite3@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}werkzeug>0:www/py-werkzeug@${PY_FLAVOR}

RUN_DEPENDS=	\
		${PYTHON_PKGNAMEPREFIX}appdirs>0:devel/py-appdirs@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}cryptography>0:security/py-cryptography@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}docutils>0:textproc/py-docutils@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}Flask>0:www/py-flask@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}gevent-websocket>0:www/py-gevent-websocket@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}Jinja2>0:devel/py-Jinja2@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}kafka-python>0:net/py-kafka-python@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}openssl>0:security/py-openssl@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}packaging>0:devel/py-packaging@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}psutil>0:sysutils/py-psutil@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}requests>0:www/py-requests@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}sqlite3>=2.7.8:databases/py-sqlite3@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}werkzeug>0:www/py-werkzeug@${PY_FLAVOR}

SHEBANG_FILES=	agent/filename.py \
		agent/ncpa_listener.py \
		agent/ncpa_passive.py

NCPADIR=	${PREFIX}/ncpa
ETCDIR=		${NCPADIR}/etc

SUB_FILES=	pkg-message ncpa_listener ncpa_passive
SUB_LIST=	NCPADIR=${NCPADIR}

NO_BUILD=	true
#do-build:
#	cd ${WRKSRC}/agent && python2.7 setup_posix.py build_exe

# ./agent/build/exe.freebsd-13.0-CURRENT-amd64-2.7/ncpa_listener
do-install:
	${MKDIR} ${STAGEDIR}${PREFIX}/ncpa
	${INSTALL} ${WRKSRC}/agent/ncpa_listener.py ${STAGEDIR}${NCPADIR}/
	${INSTALL} ${WRKSRC}/agent/ncpa_passive.py  ${STAGEDIR}${NCPADIR}/
	${INSTALL} ${WRKSRC}/agent/ncpadaemon.py  ${STAGEDIR}${NCPADIR}/
	${INSTALL} ${WRKSRC}/agent/filename.py  ${STAGEDIR}${NCPADIR}/
	${INSTALL} -d ${STAGEDIR}${NCPADIR}/listener/
.for f in __init__.py certificate.py database.py environment.py nodes.py pluginnodes.py processes.py psapi.py server.py services.py
	${INSTALL} ${WRKSRC}/agent/listener/${f}  ${STAGEDIR}${NCPADIR}/listener/
.endfor
	${INSTALL} -d ${STAGEDIR}${NCPADIR}/passive/
.for f in __init__.py kafkaproducer.py nagioshandler.py ncpacheck.py nrdp.py nrds.py utils.py
	${INSTALL} ${WRKSRC}/agent/passive/${f}  ${STAGEDIR}${NCPADIR}/passive/
.endfor
	${INSTALL} -d ${STAGEDIR}${ETCDIR}/
	${INSTALL} ${WRKSRC}/agent/etc/ncpa.cfg ${STAGEDIR}${ETCDIR}/ncpa.cfg.sample
	${INSTALL} -d ${STAGEDIR}${ETCDIR}/ncpa.cfg.d
	${INSTALL} ${WRKSRC}/agent/etc/ncpa.cfg.d/README.txt  ${STAGEDIR}${ETCDIR}/ncpa.cfg.d/
	${INSTALL} ${WRKSRC}/agent/etc/ncpa.cfg.d/example.cfg ${STAGEDIR}${ETCDIR}/ncpa.cfg.d/
.for d in css fonts help img js
	${INSTALL} -d ${STAGEDIR}${NCPADIR}/listener/static/${d}
	${INSTALL} ${WRKSRC}/agent/listener/static/${d}/* ${STAGEDIR}${NCPADIR}/listener/static/${d}/
.endfor
.for d in admin errors gui
	${INSTALL} -d ${STAGEDIR}${NCPADIR}/listener/templates/${d}
	${INSTALL} ${WRKSRC}/agent/listener/templates/${d}/* ${STAGEDIR}${NCPADIR}/listener/templates/${d}/
.endfor
	${INSTALL} ${WRKSRC}/agent/listener/templates/*.html ${STAGEDIR}${NCPADIR}/listener/templates/
	${INSTALL} -d ${STAGEDIR}${NCPADIR}/var/run
	${INSTALL} -d ${STAGEDIR}${NCPADIR}/var/log

.include <bsd.port.mk>
