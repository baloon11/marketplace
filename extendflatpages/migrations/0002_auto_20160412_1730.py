# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-12 14:30
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings


def add_documents(apps, schema_editor):
    Page = apps.get_model("extendflatpages", "ExtendFlatpage")
    Site = apps.get_model("sites", "Site")
    site = Site.objects.get(id=settings.SITE_ID)

    offer = Page(
        url='/offer/',
        title="Публичный договор оказания услуг",
        content="""
<p><strong>ПУБЛИЧНЫЙ ДОГОВОР ОКАЗАНИЯ УСЛУГ</strong></p>

<p>&nbsp;</p>

<p>НАСТОЯЩИЙ ПУБЛИЧНЫЙ ДОГОВОР (ДАЛЕЕ ИМЕНУЕМЫЙ ПО ТЕКСТУ &laquo;ДОГОВОР&raquo;) ОПРЕДЕЛЯЕТ ПОРЯДОК ОКАЗАНИЯ УСЛУГ, А ТАКЖЕ ВЗАИМНЫЕ ПРАВА, ОБЯЗАННОСТИ И ПОРЯДОК ВЗАИМООТНОШЕНИЙ МЕЖДУ ИП Тамбовцевым Сергеем Дмитриевичем, ИМЕНУЕМЫМ В ДАЛЬНЕЙШЕМ &laquo;ИСПОЛНИТЕЛЬ&raquo;, ДЕЙСТВУЮЩИЙ НА ОСНОВАНИИ СВИДЕТЕЛЬСТВА О РЕГИСТРАЦИИ, И ЗАКАЗЧИКОМ УСЛУГИ, ИМЕНУЕМЫМ В ДАЛЬНЕЙШЕМ &laquo;ЗАКАЗЧИК&raquo;, ПРИНЯВШИМ (АКЦЕПТОВАВШИМ) ПУБЛИЧНОЕ ПРЕДЛОЖЕНИЕ (ОФЕРТУ) О ЗАКЛЮЧЕНИИ НАСТОЯЩЕГО ДОГОВОРА.</p>

<p>&nbsp;</p>

<p><strong>1. ПРЕДМЕТ ДОГОВОРА</strong></p>

<p>1.1. ЗАКАЗЧИК ОБЯЗУЕТСЯ ОПЛАТИТЬ, А ИСПОЛНИТЕЛЬ ОБЯЗУЕТСЯ ОКАЗАТЬ УСЛУГУ (ДАЛЕЕ &ndash; УСЛУГА).</p>

<p>1.2. ВИД, КОЛИЧЕСТВО, КАТЕГОРИЯ И СТОИМОСТЬ УСЛУГ УКАЗАНЫ ПО АДРЕСУ: (ссылка на тарифы)</p>

<p>1.3. В ПРОЦЕССЕ ФОРМИРОВАНИЯ ЗАКАЗА ЗАКАЗЧИК ВЫБИРАЕТ тарифный план</p>

<p>1.4. ПОСЛЕ ВЫБОРА СООТВЕТСТВУЮЩЕЙ УСЛУГИ, ЗАКАЗЧИК НАЖИМАЕТ КНОПКУ &laquo;купить&raquo;. СФОРМИРОВАННАЯ ЦЕНА ЯВЛЯЕТСЯ СУММОЙ, КОТОРУЮ ЗАКАЗЧИК ДОЛЖЕН УПЛАТИТЬ ЗА ПРИОБРЕТЕНИЕ УСЛУГИ.</p>

<p>1.5. НА СТРАНИЦЕ ОФОРМЛЕНИЯ ЗАКАЗА ЗАКАЗЧИКУ НЕОБХОДИМО ОЗНАКОМИТЬСЯ С НАСТОЯЩИМ ДОГОВОРОМ.</p>

<p>1.6. ОПЛАТА УСЛУГИ ЯВЛЯЕТСЯ ПОДТВЕРЖДЕНИЕМ СОГЛАСИЯ С УСЛОВИЯМИ НАСТОЯЩЕГО ДОГОВОРА.</p>

<p>1.7. КАЖДАЯ СТОРОНА ГАРАНТИРУЕТ ДРУГОЙ СТОРОНЕ, ЧТО ОБЛАДАЕТ НЕОБХОДИМЫМИ ПРАВО - И ДЕЕСПОСОБНОСТЬЮ, А РАВНО ВСЕМИ ПРАВАМИ И ПОЛНОМОЧИЯМИ, НЕОБХОДИМЫМИ И ДОСТАТОЧНЫМИ ДЛЯ ЗАКЛЮЧЕНИЯ И ИСПОЛНЕНИЯ НАСТОЯЩЕГО ДОГОВОРА.</p>

<p>&nbsp;</p>

<p><strong>2. ПОРЯДОК ЗАКЛЮЧЕНИЯ ДОГОВОРА</strong></p>

<p>2.1. НАСТОЯЩИЙ ДОГОВОР ЯВЛЯЕТСЯ ПУБЛИЧНЫМ ДОГОВОРОМ, В СООТВЕТСТВИИ С КОТОРЫМ ИСПОЛНИТЕЛЬ ПРИНИМАЕТ НА СЕБЯ ОБЯЗАТЕЛЬСТВО ОКАЗЫВАТЬ УСЛУГИ НЕОПРЕДЕЛЕННОМУ КРУГУ ЛИЦ (ЗАКАЗЧИКИ), ОБРАТИВШИХСЯ ДЛЯ ПРИОБРЕТЕНИЯ УСЛУГ.</p>

<p>2.2. ПУБЛИКАЦИЯ (РАЗМЕЩЕНИЕ) ТЕКСТА НАСТОЯЩЕГО ДОГОВОРА НА САЙТЕ ПО СЛЕДУЮЩЕМУ АДРЕСУ: (страница оферты) ЯВЛЯЕТСЯ ПУБЛИЧНЫМ ПРЕДЛОЖЕНИЕМ (ОФЕРТОЙ) ИСПОЛНИТЕЛЯ, АДРЕСОВАННЫМ НЕОПРЕДЕЛЕННОМУ КРУГУ ЛИЦ ЗАКЛЮЧИТЬ НАСТОЯЩИЙ ДОГОВОР.</p>

<p>2.3. ЗАКЛЮЧЕНИЕ НАСТОЯЩЕГО ДОГОВОРА ПРОИЗВОДИТСЯ ПУТЕМ ПРИСОЕДИНЕНИЯ ЗАКАЗЧИКА К НАСТОЯЩЕМУ ДОГОВОРУ, Т.Е. ПОСРЕДСТВОМ ПРИНЯТИЯ (АКЦЕПТА) ЗАКАЗЧИКОМ НАСТОЯЩЕГО ДОГОВОРА В ЦЕЛОМ, БЕЗ КАКИХ-ЛИБО УСЛОВИЙ, ИЗЪЯТИЙ И ОГОВОРОК.</p>

<p>2.4. ФАКТОМ ПРИНЯТИЯ (АКЦЕПТА) ЗАКАЗЧИКОМ УСЛОВИЙ НАСТОЯЩЕГО ДОГОВОРА ЯВЛЯЕТСЯ ОПЛАТА ЗАКАЗЧИКОМ УСЛУГИ В ПОРЯДКЕ И НА УСЛОВИЯХ, ОПРЕДЕЛЕННЫХ НАСТОЯЩИМ ДОГОВОРОМ.</p>

<p>2.5. НАСТОЯЩИЙ ДОГОВОР, СЧИТАЕТСЯ ЗАКЛЮЧЕННЫМ В ПРОСТОЙ ПИСЬМЕННОЙ ФОРМЕ, НЕ ТРЕБУЕТ ОФОРМЛЕНИЯ НА БУМАГЕ И ОБЛАДАЕТ ПОЛНОЙ ЮРИДИЧЕСКОЙ СИЛОЙ.</p>

<p>&nbsp;</p>

<p><strong>3. ПРАВА И ОБЯЗАННОСТИ СТОРОН</strong></p>

<p>3.1. ИСПОЛНИТЕЛЬ ОБЯЗУЕТСЯ:</p>

<p>3.1.1. ОКАЗАТЬ ЗАКАЗЧИКУ УСЛУГУ, ВИД И ЦЕНА КОТОРОЙ ОПРЕДЕЛЯЮТСЯ В СООТВЕТСТВИИ С ГЛАВОЙ 1 НАСТОЯЩЕГО ДОГОВОРА.</p>

<p>3.1.2. ОКАЗАТЬ ЗАКАЗЧИКУ УСЛУГУ СПОСОБОМ, ОПРЕДЕЛЕННЫМ ЗАКАЗЧИКОМ ПРИ ЗАКЛЮЧЕНИИ НАСТОЯЩЕГО ДОГОВОРА.</p>

<p>3.1.3. ПРЕДПРИНИМАТЬ ВСЕ РАЗУМНЫЕ УСИЛИЯ ДЛЯ ДОЛЖНОГО ОКАЗАНИЯ УСЛУГ, ОДНАКО НЕ ОТВЕЧАЕТ ЗА НЕВОЗМОЖНОСТЬ ОКАЗАНИЯ УСЛУГ В СЛУЧАЕ НЕРАБОТОСПОСОБНОСТИ ОБОРУДОВАНИЯ ЗАКАЗЧИКА, НЕИСПРАВНОСТЬЮ ЛИНИЙ СВЯЗИ ОТ ЗАКАЗЧИКА ДО ОБОРУДОВАНИЯ ИСПОЛНИТЕЛЯ. А ТАКЖЕ ТЕХНОЛОГИЧЕСКИХ НЕИСПРАВНОСТЕЙ КАНАЛОВ СВЯЗИ ОБЩЕГО ПОЛЬЗОВАНИЯ, ПОСРЕДСТВОМ КОТОРЫХ ОСУЩЕСТВЛЯЕТСЯ ДОСТУП К УСЛУГАМ, ИЛИ УТРАТЫ ДОСТУПА В СЕТИ ИНТЕРНЕТ &mdash; ДО УСТРАНЕНИЯ НЕИСПРАВНОСТЕЙ ИЛИ ВОССТАНОВЛЕНИЯ ДОСТУПА, СООТВЕТСТВЕННО. В СЛУЧАЯХ, ПОДПАДАЮЩИХ ПОД ОПРЕДЕЛЕНИЕ ОБСТОЯТЕЛЬСТВ НЕПРЕОДОЛИМОЙ СИЛЫ</p>

<p>3.2. ЗАКАЗЧИК ОБЯЗУЕТСЯ:</p>

<p>3.2.1. ПРОИЗВЕСТИ ОПЛАТУ ЗА УСЛУГУ СОГЛАСНО НАСТОЯЩЕМУ ДОГОВОРУ И СЧЕТу НА ОПЛАТУ ДЛЯ ЮРИДИЧЕСКИХ ЛИЦ. .</p>

<p>3.2.2. ПРИ ЗАПОЛНЕНИИ ФОРМЫ ЗАКАЗА НА САЙТЕ ДЛЯ ПРИОБРЕТЕНИЯ УСЛУГИ В ОБЯЗАТЕЛЬНОМ ПОРЯДКЕ ЗАПОЛНИТЬ ВСЕ ГРАФЫ.</p>

<p>3.2.3. СОБЛЮДАТЬ ВСЕ ТРЕБОВАНИЯ И ПРАВИЛА, РАЗМЕЩЕННЫЕ НА САЙТЕ</p>

<p>&nbsp;</p>

<p><strong>3.3. ИСПОЛНИТЕЛЬ ВПРАВЕ:</strong></p>

<p>3.3.1. В ЛЮБОЙ МОМЕНТ МЕНЯТЬ УСЛОВИЯ НАСТОЯЩЕГО ДОГОВОРА БЕЗ ПРЕДВАРИТЕЛЬНОГО УВЕДОМЛЕНИЯ ТРЕТЬИХ ЛИЦ. ИЗМЕНЕНИЕ УСЛОВИЙ ДОГОВОРА НЕ ЗАТРАГИВАЕТ ПРАВА И ОБЯЗАННОСТИ ЗАКАЗЧИКА, ОПЛАТИВШЕГО УСЛУГУ.</p>

<p>3.3.2. ОТКАЗАТЬ ЗАКАЗЧИКУ В ОКАЗАНИИ УСЛУГИ ПРИ НАЛИЧИИ ЛЮБОЙ ИЗ СЛЕДУЮЩИХ ПРИЧИН:</p>

<p>3.3.2.1. ЗАКАЗЧИК НЕ ОПЛАТИЛ ПОЛНОСТЬЮ ЛИБО ЧАСТИЧНО СТОИМОСТЬ УСЛУГИ;</p>

<p>3.3.2.2. ЗАКАЗЧИК НЕ ЗАПОЛНИЛ ДАННЫЕ ФОРМЫ ЗАКАЗА В СООТВЕТСТВИИ С П. 3.2.2. НАСТОЯЩЕГО ДОГОВОРА;</p>

<p>3.3.2.3. ЗАКАЗЧИК НАРУШИЛ ТРЕБОВАНИЯ И ПРАВИЛА, РАСПОЛОЖЕННЫЕ ПО АДРЕСУ (ссылка на правила оформления товаров)</p>

<p>3.3.2.4. ЗАКАЗЧИК ПРИ ЗАПОЛНЕНИИ ФОРМЫ ЗАКАЗА УКАЗАЛ ИНФОРМАЦИЮ СЛЕДУЮЩЕГО СОДЕРЖАНИЯ:</p>

<p>- СОДЕРЖАЩИЕ НЕНОРМАТИВНУЮ ЛЕКСИКУ, А ТАКЖЕ ОСКОРБИТЕЛЬНЫЕ ВЫСКАЗЫВАНИЯ, В Т.Ч. РАСИСТСКОГО И РЕЛИГИОЗНОГО ХАРАКТЕРА;</p>

<p>- С ПРИЗЫВОМ К НАСИЛИЮ И ПРОТИВОПРАВНЫМ ДЕЙСТВИЯМ;</p>

<p>- О ДИСКРИМИНАЦИИ ПО НАЦИОНАЛЬНОМУ, РАСОВОМУ, РЕЛИГИОЗНОМУ, ПОЛОВОМУ И ДРУГИМ ПРИЗНАКАМ;</p>

<p>- НАРУШАЮЩИЕ ОБЩЕПРИНЯТЫЕ НОРМЫ МОРАЛИ И НРАВСТВЕННОСТИ;</p>

<p>- О ПОРНОГРАФИИ, В Т.Ч. ФОТО ПОРНОГРАФИЧЕСКОГО ХАРАКТЕРА;</p>

<p>- О МОШЕННИЧЕСТВЕ И ВЫМОГАТЕЛЬСТВЕ;</p>

<p>- С ПРОСЬБОЙ О ПРЕДОПЛАТЕ, ПОЧТОВОЙ ПЕРЕСЫЛКЕ НАЛОЖЕННЫМ ПЛАТЕЖОМ ИЛИ В КОНВЕРТЕ ДЕНЕЖНЫХ СУММ, А ТАКЖЕ ДРУГИХ ВЛОЖЕНИЙ;</p>

<p>- О ПРИГЛАШЕНИИ НА РАБОТУ И УЧЕБУ ЗА ГРАНИЦЕЙ;</p>

<p>- ОБ ОКАЗАНИИ МЕДИЦИНСКИХ УСЛУГ ЧАСТНЫМИ ЛИЦАМИ;</p>

<p>- О ЗНАКОМСТВАХ;</p>

<p>- О ПОКУПКЕ-ПРОДАЖЕ:</p>

<p>&bull; ИНОСТРАННОЙ ВАЛЮТЫ;</p>

<p>&bull; ГОСУДАРСТВЕННЫХ НАГРАД;</p>

<p>&bull; ПЕРСОНАЛЬНЫХ ДОКУМЕНТОВ, А ТАКЖЕ БЛАНКОВ ЭТИХ ДОКУМЕНТОВ;</p>

<p>&bull; ВСЕХ ВИДОВ ОРУЖИЯ И СРЕДСТВ АКТИВНОЙ ЗАЩИТЫ;</p>

<p>&bull; НАРКОТИЧЕСКИХ И ОТРАВЛЯЮЩИХ ВЕЩЕСТВ;</p>

<p>&bull; СПИРТНЫХ НАПИТКОВ, ТАБАЧНЫХ ИЗДЕЛИЙ;</p>

<p>&bull; ЧЕЛОВЕЧЕСКИХ ОРГАНОВ;</p>

<p>&bull; ПРОДАЖЕ ЛЕКАРСТВЕННЫХ ПРЕПАРАТОВ И БИОЛОГИЧЕСКИ АКТИВНЫХ ПИЩЕВЫХ ДОБАВОК;</p>

<p>&bull; ПРОДАЖЕ ЮВЕЛИРНЫХ ИЗДЕЛИЙ;</p>

<p>3.3.3. ОТКАЗАТЬ ЗАКАЗЧИКУ В ВОЗВРАТЕ ДЕНЕЖНЫХ СРЕДСТВ, В СЛУЧАЯХ, УКАЗАННЫХ&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; В П.&nbsp; 3.3.2 НАСТОЯЩЕГО ДОГОВОРА.</p>

<p>3.3.4. ИСПОЛЬЗОВАТЬ АДРЕС ЭЛЕКТРОННОЙ ПОЧТЫ, УКАЗАННЫЙ ЗАКАЗЧИКОМ, ДЛЯ ИНФОРМИРОВАНИЯ ПОСЛЕДНЕГО О НОВЫХ УСЛУГАХ И ТОВАРАХ, ПРЕДЛАГАЕМЫХ ИСПОЛНИТЕЛЕМ.</p>

<p>&nbsp;</p>

<p>4<strong>.РАЗРЕШЕНИЕ СПОРОВ</strong></p>

<p>4.1. ВСЕ СПОРЫ, ВОЗНИКАЮЩИЕ ПРИ ИСПОЛНЕНИИ НАСТОЯЩЕГО ДОГОВОРА, ПОДЛЕЖАТ РАЗРЕШЕНИЮ ПУТЕМ ПЕРЕГОВОРОВ.</p>

<p>4.2. В СЛУЧАЕ ЕСЛИ СПОР, ВОЗНИКШИЙ МЕЖДУ СТОРОНАМИ, НЕ МОЖЕТ БЫТЬ РАЗРЕШЕН ПУТЕМ ПЕРЕГОВОРОВ, ОН ПЕРЕДАЕТСЯ НА РАССМОТРЕНИЕ СУДА СОГЛАСНО ДЕЙСТВУЮЩЕМУ ЗАКОНОДАТЕЛЬСТВУ Российской федерации.</p>

<p>&nbsp;</p>

<p><strong>5.ПОРЯДОК СДАЧИ-ПРИЕМКИ РАБОТ</strong></p>

<p>5.1. ВЫПОЛНЕНИЕ УСЛУГ ПОДТВЕРЖДАЕТСЯ АКТОМ ВЫПОЛНЕННЫХ РАБОТ (ОТЧЕТОМ) В ЭЛЕКТРОННОМ ВАРИАНТЕ.</p>

<p>5.2. В СЛУЧАЕ ЕСЛИ АКТЫ ПРИЕМКИ-ПЕРЕДАЧИ ВЫПОЛНЕННЫХ УСЛУГ НЕ БУДУТ ПОДПИСАНЫ ЗАКАЗЧИКОМ БЕЗ ОБОСНОВАННЫХ ПИСЬМЕННЫХ ЗАМЕЧАНИЙ НА ПРОТЯЖЕНИИ 5 (ПЯТИ) КАЛЕНДАРНЫХ ДНЕЙ С МОМЕНТА ПОЛУЧЕНИЯ АКТА, ТАКИЕ УСЛУГИ СЧИТАЮТСЯ ВЫПОЛНЕННЫМИ.</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong>6.СТОИМОСТЬ УСЛУГ</strong></p>

<p>6.1. СТОИМОСТЬ УСЛУГ ИСПОЛНИТЕЛЯ ОПРЕДЕЛЯЕТСЯ НА ОСНОВАНИИ ДАННЫХ, РАЗМЕЩЕННЫХ НА САЙТЕ ИСПОЛНИТЕЛЯ, И СООБЩАЕТСЯ ЗАКАЗЧИКУ ПРИ ЗАВЕРШЕНИИ ОФОРМЛЕНИЯ ЗАКАЗА УСЛУГИ. СООБЩЕННАЯ ТАКИМ ОБРАЗОМ СТОИМОСТЬ УСЛУГИ ЯВЛЯЕТСЯ ОКОНЧАТЕЛЬНОЙ И ПОДЛЕЖАЩЕЙ ОПЛАТЕ ДЛЯ ПОЛУЧЕНИЯ ЗАКАЗЧИКОМ УСЛУГИ.</p>

<p>6.2. СТОИМОСТЬ УСЛУГИ, ОКАЗЫВАЕМОЙ ЗАКАЗЧИКУ ПО НАСТОЯЩЕМУ ДОГОВОРУ ФОРМИРУЕТСЯ В ПОРЯДКЕ, УКАЗАННОМ В ГЛАВЕ 1 НАСТОЯЩЕГО ДОГОВОРА.</p>

<p>&nbsp;</p>

<p><strong>7. УСЛОВИЯ ОПЛАТЫ</strong></p>

<p>7.1. РАСЧЕТЫ ЗА УСЛУГИ, ПРЕДОСТАВЛЯЕМЫЕ ПО НАСТОЯЩЕМУ ДОГОВОРУ, ПРОИЗВОДЯТСЯ ПО БЕЗНАЛИЧНОМУ РАСЧЕТУ ПУТЕМ 100% ПРЕДОПЛАТЫ НА РАСЧЕТНЫЙ СЧЕТ ИСПОЛНИТЕЛЯ.</p>

<p>7.2. ВЫБОР И ИСПОЛЬЗОВАНИЕ СПОСОБА ОПЛАТЫ УСЛУГ ПРОИЗВОДИТСЯ ЗАКАЗЧИКОМ ПО СОБСТВЕННОМУ УСМОТРЕНИЮ И БЕЗ КАКОЙ-ЛИБО ОТВЕТСТВЕННОСТИ ИСПОЛНИТЕЛЯ. БЕЗОПАСНОСТЬ, КОНФИДЕНЦИАЛЬНОСТЬ, А ТАКЖЕ ИНЫЕ УСЛОВИЯ ИСПОЛЬЗОВАНИЯ ВЫБРАННЫХ ЗАКАЗЧИКОМ СПОСОБОВ ОПЛАТЫ ВЫХОДЯТ ЗА РАМКИ ДАННОГО ДОГОВОРА И РЕГУЛИРУЮТСЯ СОГЛАШЕНИЯМИ МЕЖДУ ЗАКАЗЧИКОМ И СООТВЕТСТВУЮЩИМИ ОРГАНИЗАЦИЯМИ.</p>

<p>7.3. В СЛУЧАЕ ОТКАЗА ЗАКАЗЧИКОМ ОТ ОКАЗАНИЯ УСЛУГ, ИСПОЛНИТЕЛЬ ОБЯЗУЕТСЯ ВОЗВРАТИТЬ СУММУ ВНЕСЕННОЙ ПРЕДОПЛАТЫ В ТЕЧЕНИЕ 15 БАНКОВСКИХ ДНЕЙ С МОМЕНТА ОТПРАВКИ УКАЗАННОГО УВЕДОМЛЕНИЯ, УДЕРЖАВ ФАКТИЧЕСКИ ПОНЕСЕННЫЕ РАСХОДЫ ИСПОЛНИТЕЛЯ.</p>

<p>&nbsp;</p>

<p><strong>8. ПОЛИТИКА ОКАЗАНИЯ УСЛУГ</strong></p>

<p>8.1. ИСПОЛНИТЕЛЬ ОБЯЗУЕТСЯ ОКАЗАТЬ УСЛУГИ ПО НАСТОЯЩЕМУ ДОГОВОРУ В СРОК,&nbsp;НЕ ПРЕВЫШАЮЩИЙ 7 РАБОЧИХ ДНЕЙ С МОМЕНТА ПОЛУЧЕНИЯ ОПЛАТЫ ОТ ЗАКАЗЧИКА.</p>

<p>&nbsp;</p>

<p><strong>9. ДОПОЛНИТЕЛЬНЫЕ УСЛОВИЯ</strong></p>

<p>9.1. СТОРОНЫ ОСВОБОЖДАЮТСЯ ОТ ОТВЕТСТВЕННОСТИ ЗА ЧАСТИЧНОЕ ИЛИ ПОЛНОЕ НЕИСПОЛНЕНИЕ СВОИХ ОБЯЗАТЕЛЬСТВ ПО НАСТОЯЩЕМУ ДОГОВОРУ, ЕСЛИ ЭТО ЯВИЛОСЬ СЛЕДСТВИЕМ ДЕЙСТВИЯ ОБСТОЯТЕЛЬСТВ НЕПРЕОДОЛИМОЙ СИЛЫ (ФОРС-МАЖОРА), ВОЗНИКШИХ ПОСЛЕ ЗАКЛЮЧЕНИЯ НАСТОЯЩЕГО ДОГОВОРА В РЕЗУЛЬТАТЕ СОБЫТИЙ ЧРЕЗВЫЧАЙНОГО ХАРАКТЕРА, КОТОРЫЕ СТОРОНЫ НЕ МОГЛИ НИ ПРЕДВИДЕТЬ, НИ ПРЕДОТВРАТИТЬ РАЗУМНЫМИ МЕРАМИ.</p>

<p>9.2. В СЛУЧАЕ ВОЗНИКНОВЕНИЯ СПОРОВ МЕЖДУ ЗАКАЗЧИКОМ И ИСПОЛНИТЕЛЕМ ПО ВОПРОСАМ, СВЯЗАННЫМ С ИСПОЛНЕНИЕМ НАСТОЯЩЕГО ДОГОВОРА, СТОРОНЫ ПРИМУТ ВСЕ МЕРЫ К РАЗРЕШЕНИЮ ИХ ПУТЕМ ПЕРЕГОВОРОВ МЕЖДУ СОБОЙ.</p>

<p>9.3. ВСЕ ВОПРОСЫ, НЕУРЕГУЛИРОВАННЫЕ НАСТОЯЩИМ ДОГОВОРОМ, РАЗРЕШАЮТСЯ В СООТВЕТСТВИИ С ДЕЙСТВУЮЩИМ ЗАКОНОДАТЕЛЬСТВОМ российской федерации, А ТАКЖЕ ЛОКАЛЬНЫМИ НОРМАТИВНЫМИ ДОКУМЕНТАМИ ИСПОЛНИТЕЛЯ, ПРИ УСЛОВИИ ИХ СООТВЕТСТВИЯ ДЕЙСТВУЮЩЕМУ ЗАКОНОДАТЕЛЬСТВУ российской федерации.</p>

<p>9.4. НАСТОЯЩИЙ ДОГОВОР СЧИТАЕТСЯ ЗАКЛЮЧЕННЫМ С МОМЕНТА ЗАЧИСЛЕНИЯ НА РАСЧЕТНЫЙ СЧЕТ ИСПОЛНИТЕЛЯ ДЕНЕЖНЫХ СРЕДСТВ, УПЛАЧЕННЫХ ЗАКАЗЧИКОМ В СЧЕТ ОПЛАТЫ УСЛУГ В ПОРЯДКЕ И НА УСЛОВИЯХ, ОПРЕДЕЛЕННЫХ НАСТОЯЩИМ ДОГОВОРОМ.</p>

<p>9.5. ОПЛАЧИВАЯ СТОИМОСТЬ УСЛУГ, ЗАКАЗЧИК БЕЗОГОВОРОЧНО СОГЛАШАЕТСЯ С УСЛОВИЯМИ НАСТОЯЩЕГО ДОГОВОРА.</p>

<p>9.6. В СЛУЧАЕ ПРИЧИНЕНИЯ УБЫТКОВ ЗАКАЗЧИКУ ПО ВИНЕ ИСПОЛНИТЕЛЯ ИСПОЛНИТЕЛЬ НЕСЕТ ПЕРЕД ЗАКАЗЧИКОМ ОТВЕТСТВЕННОСТЬ В СУММЕ, НЕ ПРЕВЫШАЮЩЕЙ СТОИМОСТЬ ЗАКАЗАННОЙ И ОПЛАЧЕННОЙ ЗАКАЗЧИКОМ, НО НЕ ПОЛУЧЕННОЙ ПО ВИНЕ ИСПОЛНИТЕЛЯ УСЛУГИ ИЛИ, ЕСЛИ ПРИМЕНИМО, В СУММЕ, НЕ ПРЕВЫШАЮЩЕЙ БАЛАНС КОШЕЛЬКА ЗАКАЗЧИКА НА МОМЕНТ ПРИЧИНЕНИЯ УБЫТКОВ.</p>

<p>9.7. ЗАКАЗЧИК ОТВЕЧАЕТ ЗА ЛЮБЫЕ ДЕЙСТВИЯ, СОВЕРШЕННЫЕ С ИСПОЛЬЗОВАНИЕМ ЛОГИНА/ПАРОЛЯ ЗАКАЗЧИКА НА САЙТЕ В ТОМ ЧИСЛЕ ЗА ДЕЙСТВИЯ ТРЕТЬИХ ЛИЦ, А ТАКЖЕ СОХРАННОСТЬ СВОЕГО ЛОГИНА/ПАРОЛЯ И ЗА УБЫТКИ, КОТОРЫЕ МОГУТ ВОЗНИКНУТЬ ПО ПРИЧИНЕ ЕГО НЕСАНКЦИОНИРОВАННОГО ИСПОЛЬЗОВАНИЯ. В СЛУЧАЕ КРАЖИ/УТЕРИ ЛОГИНА ИЛИ ПАРОЛЯ, ЗАКАЗЧИК САМОСТОЯТЕЛЬНО ПРЕДПРИНИМАЕТ НЕОБХОДИМЫЕ МЕРЫ ДЛЯ СМЕНЫ ПАРОЛЯ ДЛЯ ДОСТУПА К УСЛУГАМ. ИСПОЛНИТЕЛЬ НЕ НЕСЕТ ОТВЕТСТВЕННОСТЬ ЗА ДЕЙСТВИЯ ТРЕТЬИХ ЛИЦ, ПОВЛЕКШУЮ КРАЖУ/УТЕРЮ ЛОГИНА ИЛИ ПАРОЛЯ ЗАКАЗЧИКА</p>

<p>9.8. ЗАКАЗЧИК ОБЯЗУЕТСЯ НЕ ПРЕДОСТАВЛЯТЬ ИНФОРМАЦИЮ, КОТОРАЯ НЕ СООТВЕТСТВУЕТ ДЕЙСТВУЮЩЕМУ ЗАКОНОДАТЕЛЬСТВУ Рф, СОДЕРЖАЩИЕ НЕДОСТОВЕРНУЮ ИНФОРМАЦИЮ ИЛИ НЕ НОРМАТИВНУЮ ЛЕКСИКУ И ДР. В СЛУЧАЕ НАРУШЕНИЯ ЗАКАЗЧИКОМ ДАННОГО ПУНКТА, ЗАКАЗЧИК НЕСЕТ ОТВЕТСТВЕННОСТЬ В СООТВЕТСТВИИ С ДЕЙСТВУЮЩИМ ЗАКОНОДАТЕЛЬСТВОМ Рф И ВОЗМЕЩАЕТ ИСПОЛНИТЕЛЮ ВСЕ ПОНЕСЕННЫЕ РАСХОДЫ, СВЯЗАННЫЕ С НАРУШЕНИЕМ ДАННОГО ПУНКТА.</p>

<p>9.9. ИСПОЛНИТЕЛЬ ОБЯЗУЕТСЯ ОБЕСПЕЧИТЬ КРУГЛОСУТОЧНУЮ ЕЖЕДНЕВНУЮ РАБОТОСПОСОБНОСТЬ СЕРВИСА В ТЕЧЕНИЕ СРОКА ДЕЙСТВИЯ НАСТОЯЩЕГО ДОГОВОРА, ЗА ИСКЛЮЧЕНИЕМ СЛУЧАЕВ ПРОВЕДЕНИЯ НЕОБХОДИМЫХ ПРОФИЛАКТИЧЕСКИХ (РЕГЛАМЕНТНЫХ) И РЕМОНТНЫХ РАБОТ, КОТОРЫЕ БУДУТ ПЛАНИРОВАТЬСЯ НА ВРЕМЯ, КОГДА ЭТО МОЖЕТ НАНЕСТИ НАИМЕНЬШИЙ УЩЕРБ ЗАКАЗЧИКУ. ПРИ ЭТОМ ИСПОЛНИТЕЛЬ НЕ НЕСЕТ ОТВЕТСТВЕННОСТЬ ЗА КАЧЕСТВО И РАБОТОСПОСОБНОСТЬ УСЛУГ, ПРЕДОСТАВЛЯЕМЫХ ОПЕРАТОРАМИ СВЯЗИ, ПЕРЕБОЯМИ В ЭЛЕКТРОПИТАНИЯХ И ПРИ ПРОЧИХ ОБСТОЯТЕЛЬСТВ, НЕ ЗАВИСЯЩИХ ОТ ИСПОЛНИТЕЛЯ В СЛУЧАЕ ПОТЕРИ ЗАКАЗЧИКОМ ЧАСТИ ИЛИ ВСЕЙ СУММЫ БАЛАНСА КОШЕЛЬКА.</p>

<p>&nbsp;</p>

<p><strong>10.РЕКВИЗИТЫ СТОРОН</strong></p>

<p>10.1. СТОРОНЫ БЕЗОГОВОРОЧНО СОГЛАШАЮТСЯ ПОД РЕКВИЗИТАМИ ЗАКАЗЧИКА СЧИТАТЬ ИНФОРМАЦИЮ, УКАЗАННУЮ ИМ ПРИ ОПЛАТЕ УСЛУГ.</p>

<p>10.2. РЕКВИЗИТЫ ИСПОЛНИТЕЛЯ:</p>

<p>ИП Тамбовцев Сергей Дмитриевич</p>

<p>Г. Иркутск, Байкальская 126а, 103</p>

<p>ТЕЛ.: +7 / 999 / 641-87-95</p>

<p>ИнН: 753615321277</p>

<p>Счет: 40802810223470000142</p>

<p>БИК: 045004774</p>

<p>В ФИЛИАЛЕ &laquo;Новосибирский&raquo; АО &laquo;альфа банк&raquo;</p>

<p>&nbsp;</p>
        """,
        template_name="flatpages/default.html"
    )
    offer.save()
    offer.sites.add(site)

    terms = Page(
        url='/terms/',
        title="Условия размещения объявлений",
        content="""
<p>Условия размещения объявлений</p>

<p>Настоящие Условия могут быть в&nbsp;любое время изменены без уведомления Пользователя. Использование сервиса после внесения соответствующих изменений означает безоговорочное согласие с&nbsp;ними Пользователя и&nbsp;устанавливает для него соответствующие обязательства и&nbsp;ответственность за&nbsp;соблюдение Условий.</p>

<p>1. Общие положения</p>

<p>Сайт Youstore предоставляет Пользователю возможность осуществлять размещение Объявлений о&nbsp;Товаре на&nbsp;условиях и&nbsp;с&nbsp;соблюдением требований, установленных настоящими Условиями и&nbsp;Договором на оказание услуг.</p>

<p>Размещение Объявлений осуществляется любым Пользователем, зарегистрированным в&nbsp;установленном порядке на&nbsp;Сайте Youstore.</p>

<p>Все размещаемые Пользователем Объявления, возможность их&nbsp;редактирования, удаления, снятия с&nbsp;публикации, активации, совершение иных действий с&nbsp;Объявлением доступны Пользователю в&nbsp;Личном кабинете на&nbsp;Сайте.</p>

<p>Показ размещенных в&nbsp;соответствии с&nbsp;настоящими Условиями Объявлений осуществляется в&nbsp;результатах поиска в&nbsp;общем списке одновременно с&nbsp;Объявлениями иных Пользователей, схожих по&nbsp;содержанию, запросу или иным параметрам Объявления.</p>

<p>2. Условия размещения Объявлений и&nbsp;обязательства Пользователя</p>

<p>Продавец обязуется размещать Объявления в&nbsp;соответствии с&nbsp;инструкциями и&nbsp;предоставлять точную и&nbsp;полную информацию о&nbsp;Товаре и&nbsp;условиях его продажи. Размещая Объявление, Пользователь подтверждает, что он&nbsp;имеет право распоряжаться Товаром или осуществлять в&nbsp;отношении Товара иные действия, указанные в&nbsp;Объявлении.</p>

<p>В&nbsp;целях поддержания высокого качества Сервисов, администрация сайта оставляет за&nbsp;собой право ограничить количество активных, т.е. доступных для просмотра третьими лицами Объявлений Пользователя, а&nbsp;также ограничивать действия Пользователя на&nbsp;сайте.</p>

<p>Пользователь имеет право реализовывать на&nbsp;сайте принадлежащие ему Товары, при условии, что для этого не&nbsp;требуется специальных разрешений, а&nbsp;также при условии соблюдения действующего Договора на оказание услуг.</p>

<p>На&nbsp;сайте запрещены Объявления о&nbsp;Товарах, продажа которых нарушает действующее законодательство Российской Федерации, противоречит общепринятым нормам морали, является оскорбительной или неуместной.</p>

<p>Пользователь обязан самостоятельно удостовериться, что продажа Товара не&nbsp;нарушает положений действующего законодательства.</p>

<p>Продавец обязан тщательно проверять всю информацию о&nbsp;Товаре, указанном в&nbsp;Объявлении, и, в&nbsp;случае обнаружения неверной и/или неполной информации, добавлять необходимые сведения в&nbsp;описание и/или условия продажи Товара в&nbsp;Объявлении или исправлять неверную информацию, отредактировав Объявление.</p>

<p>Описание Товара, указанное Продавцом в&nbsp;Объявлении, его стоимость и&nbsp;предложение заключения сделки в&nbsp;отношении Товара составляют условия продажи этого Товара.</p>

<p>В&nbsp;Объявлениях запрещено оставлять любые ссылки на&nbsp;страницы Интернет-сайтов, за&nbsp;исключением случаев, когда такие ссылки необходимы в&nbsp;целях выполнения требований действующего законодательства Российской Федерации.</p>

<p>Условия продажи и&nbsp;описание Товара, указанные в&nbsp;Объявлении, не&nbsp;должны противоречить действующему законодательству и&nbsp;Договору на оказание услуг, как на&nbsp;момент размещения Объявления, так и&nbsp;в&nbsp;дальнейшем, включая возможные изменения Объявления, изменение положений действующего законодательства Российской Федерации и&nbsp;иные обстоятельства.</p>

<p>Сайт имеет право переместить, завершить или продлить срок демонстрации Объявления по&nbsp;техническим причинам, находящимся под контролем или вне контроля администрации.</p>

<p>Администрация сайта имеет право прекратить демонстрацию любого Объявления в&nbsp;любое время.</p>

<p>3. Предоставляемые Пользователем сведения при размещении Объявлений</p>

<p>Сведения, предоставляемые Пользователем при размещении Объявлений должны быть полными, достоверными, соответствующими предлагаемому Товару и&nbsp;действительным намерениям Продавца в&nbsp;отношении такого Товара, не&nbsp;допускающими неоднозначного или двойного понимания.</p>

<p>Ограничения.</p>

<p>Сведения, предоставленные Пользователем, в&nbsp;том числе при размещении Объявлений, и&nbsp;любые его действия не&nbsp;должны:</p>

<p>быть ложными, неточными или вводящими в&nbsp;заблуждение;</p>

<p>способствовать мошенничеству, обману или злоупотреблению доверием;</p>

<p>вести к&nbsp;совершению сделок с&nbsp;крадеными или поддельными предметами;</p>

<p>нарушать или посягать на&nbsp;собственность третьего лица, его коммерческую тайну либо его право на&nbsp;неприкосновенность частной жизни;</p>

<p>содержать сведения, оскорбляющие чью-либо честь, достоинство или деловую репутацию;</p>

<p>содержать клевету или угрозы кому&nbsp;бы то&nbsp;ни&nbsp;было;</p>

<p>призывать к&nbsp;совершению преступления, а&nbsp;также разжигать межнациональную рознь;</p>

<p>способствовать, поддерживать или призывать к&nbsp;террористической и&nbsp;экстремистской деятельности;</p>

<p>быть непристойными либо носить характер порнографии;</p>

<p>содержать компьютерные вирусы, а&nbsp;также иные компьютерные программы, направленные, в&nbsp;частности, на&nbsp;нанесение вреда, неуполномоченное вторжение, тайный перехват либо присвоение данных любой системы, либо самой системы, либо ее&nbsp;части, либо личной информации или иных данных;</p>

<p>причинять вред сайту, а&nbsp;также становиться причиной полной либо частичной потери услуг провайдеров сети Интернет, либо услуг любых иных лиц;</p>

<p>содержать материалы рекламного характера;</p>

<p>нарушать интеллектуальные права третьих лиц, право на&nbsp;изображение гражданина и&nbsp;иные материальные и&nbsp;нематериальные права третьих лиц;</p>

<p>иным образом нарушать действующее законодательство Российской Федерации.</p>

<p>4. Соответствие требованиям</p>

<p>Администрация сайта может выборочно осуществлять проверку Объявлений на&nbsp;соответствие требованиям настоящих Условий и&nbsp;Пользовательского соглашения на&nbsp;любом этапе размещения Объявления, как в&nbsp;момент создания и&nbsp;отправки Объявления для публикации, так и&nbsp;в&nbsp;процессе его показа на&nbsp;Сайте Youstore.</p>

<p>При обнаружении в&nbsp;Объявлении признаков нарушения положений и&nbsp;требований действующего законодательства Российской Федерации администрация сайта вправе отказать в&nbsp;размещении Объявления&nbsp;&mdash; прекратить показ Объявления, заблокировать его и&nbsp;предоставить Пользователю возможность устранить допущенные нарушения, заблокировать Объявления без возможности его редактирования, а&nbsp;также ограничить и/или заблокировать Пользователю доступ в&nbsp;его Личный кабинет.</p>

<p>5. Гарантии и&nbsp;ответственность</p>

<p>Пользователь несет ответственность за&nbsp;соблюдение положений действующего законодательства Российской Федерации при использовании сервиса размещения Объявлений, предусмотренных настоящими Условиями, Пользовательским соглашением и&nbsp;иными положениями, установленными и&nbsp;размещенными на&nbsp;Сайте.</p>

<p>Осуществляя размещение Объявления в&nbsp;соответствии с&nbsp;настоящими Условиями, Пользователь гарантирует, что обладает необходимыми правами на&nbsp;Товар, в&nbsp;отношении которого размещается предложение, на&nbsp;любые действия с&nbsp;таким Товаром, включая размещение соответствующей информации о&nbsp;Товаре на&nbsp;Сайте.</p>

<p>Пользователь единолично несет ответственность за&nbsp;реализацию Товаров, предложения о&nbsp;которых размещаются им&nbsp;на сайте и&nbsp;любые ее&nbsp;последствия.</p>

<p>Сайт Youstore не&nbsp;является Продавцом и/или посредником сделок, совершаемых Пользователями исходя из&nbsp;информации, полученной на&nbsp;сайте, в&nbsp;связи с&nbsp;чем не&nbsp;несет ответственности за&nbsp;любые сделки, заключенные между Пользователями при использовании сайта, и&nbsp;их&nbsp;последствия.</p>

<p>Пользователь несет ответственность за&nbsp;соответствие Товара заявленным в&nbsp;Объявлении характеристикам, качеству, безопасности, а&nbsp;также за&nbsp;законность и&nbsp;возможность Продавца продать Товар.</p>

<p>Все претензии к&nbsp;Товару, к&nbsp;содержанию Объявления, информации Пользователя и&nbsp;любые иные требования к&nbsp;Продавцу в&nbsp;рамках заключаемых с&nbsp;таким Продавцом сделок, на&nbsp;основании информации, размещенной Продавцом на&nbsp;Сайте, разрешаются Продавцом своими силами и&nbsp;за&nbsp;свой счет, без участия администрации сайта.</p>

<p>&nbsp;</p>
        """,
        template_name="flatpages/default.html"
    )
    terms.save()
    terms.sites.add(site)


class Migration(migrations.Migration):

    dependencies = [
        ('extendflatpages', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_documents),
    ]
