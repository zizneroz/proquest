from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree
from zipfile import ZipFile
from os.path import basename
import paramiko

class CreateXML:
    def indent(self, elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def csv_to_xml(self,file, filename):
        if file.name.endswith('.csv'):
            file_data = file.read().decode("utf-8")		
            lines = file_data.splitlines()

            for index, line in enumerate(lines):
                if index == 3:
                    fields = line.split(",")

                    submission = Element('DISS_submission', publishing_option=fields[1], embargo_code=fields[2], third_party_search=fields[3])
                    
                    authorship = SubElement(submission, 'DISS_authorship')
                    author = SubElement(authorship, 'DISS_author', type=fields[4])
                    name = SubElement(author, 'DISS_name')
                    SubElement(name, 'DISS_surname').text = fields[5]
                    SubElement(name, 'DISS_fname').text = fields[6]
                    SubElement(name, 'DISS_middle').text = ''

                    description = SubElement(submission, 'DISS_description', page_count=fields[7], type=fields[8], external_id=fields[9], apply_for_copyright=fields[10])
                    SubElement(description, 'DISS_title').text = fields[11]
                    dates = SubElement(description, 'DISS_dates')
                    SubElement(dates, 'DISS_comp_date').text = fields[12]
                    SubElement(dates, 'DISS_accept_date').text = ''
                    SubElement(description, 'DISS_language').text = fields[15]
                    SubElement(description, 'DISS_degree').text = fields[16]
                    institution = SubElement(description, 'DISS_institution')
                    SubElement(institution, 'DISS_inst_code').text = '2063'
                    SubElement(institution, 'DISS_inst_name').text = fields[18]
                    SubElement(institution, 'DISS_processing_code').text = fields[19]

                    content = SubElement(submission, 'DISS_content')
                    abstract = SubElement(content, 'DISS_abstract')
                    SubElement(abstract, 'DISS_para').text = ''
                    SubElement(content, 'DISS_binary', type=fields[20]).text = fields[21]
                    self.indent(submission)
                    xml_file = ElementTree(submission)
                    xml_name = '%s_%s_DATA.xml'% (fields[5],fields[6])
                    xml_file.write('media/files_created/%s'% (xml_name), encoding="UTF-8", xml_declaration=True, short_empty_elements=False, method="xml")
                    self.downloadPDF(fields[21])
                    self.createZIP(fields[21], xml_name, 'upload_%s_%s.zip' % (fields[5], fields[6]))

                    if index == 4:
                        break

        else:
            return 'Solo se aceptan archivos CSV'

    def queryset_to_xml(self, query):
        submission = Element('DISS_submission', publishing_option=query.publishing, embargo_code= query.embargo, third_party_search=query.third_party)
                    
        authorship = SubElement(submission, 'DISS_authorship')
        author = SubElement(authorship, 'DISS_author', type=query.author_type)
        name = SubElement(author, 'DISS_name')
        SubElement(name, 'DISS_surname').text = query.surname
        SubElement(name, 'DISS_fname').text = query.fname
        SubElement(name, 'DISS_middle').text = ''

        description = SubElement(submission, 'DISS_description', page_count=query.page_count, type=query.page_type, external_id=query.external_id, apply_for_copyright=query.apply_copyright)
        SubElement(description, 'DISS_title').text = query.title
        dates = SubElement(description, 'DISS_dates')
        SubElement(dates, 'DISS_comp_date').text = query.comp_date
        SubElement(dates, 'DISS_accept_date').text = query.accept_date
        SubElement(description, 'DISS_language').text = query.languaje
        SubElement(description, 'DISS_degree').text = query.degree
        institution = SubElement(description, 'DISS_institution')
        SubElement(institution, 'DISS_inst_code').text = query.inst_code
        SubElement(institution, 'DISS_inst_name').text = query.inst_name
        SubElement(institution, 'DISS_processing_code').text = query.processing_code

        content = SubElement(submission, 'DISS_content')
        abstract = SubElement(content, 'DISS_abstract')
        SubElement(abstract, 'DISS_para').text = query.para
        SubElement(content, 'DISS_binary', type=query.binary_type).text = query.binary
        self.indent(submission)
        xml_file = ElementTree(submission)
        xml_name = '%s_%s_DATA.xml'% (query.surname,query.fname)
        xml_file.write('media/files_created/%s'% (xml_name), encoding="UTF-8", xml_declaration=True, short_empty_elements=False, method="xml")
        self.downloadPDF(query.binary)
        zip_name = 'upload_%s_%s.zip' % (query.surname, query.fname)
        self.createZIP(query.binary, xml_name, zip_name)
        return zip_name
    
    def downloadPDF(self, filename):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('000.00.00.000', username = 'xxxxxxx', password='*******')
        sftp = ssh.open_sftp()
        localpath = 'media/files_pdf/%s' % (filename)
        remotepath = '/datos/pdfs/%s' % (filename)
        sftp.get(remotepath, localpath)
        sftp.close()
        ssh.close()
    
    def createZIP(self, pdf_name, xml_name, zip_name):
        zf = ZipFile('media/files_zip/%s' % (zip_name), mode='w')
        xml_path = 'media/files_created/%s' % (xml_name)
        pdf_path = 'media/files_pdf/%s' % (pdf_name)
        try:
            zf.write(xml_path, basename(xml_path))
            zf.write(pdf_path, basename(pdf_path))
        finally:
            zf.close()
