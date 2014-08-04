import urlparse

# Python 2.5+ provides urllib2.quote, whereas Python 2.4 only
# provides urllib.quote.
try:
    from urllib2 import quote as urllib_quote
except ImportError:
    from urllib import quote as urllib_quote
from reviewboard.scmtools.errors import FileNotFoundError, \
                                        InvalidRevisionFormatError, \
                                        RepositoryNotFoundError, \
                                        SCMError
urlparse.uses_netloc.append('git')
            detail='The SHA1 is too short. Make sure the diff is generated '
                   'with `git diff --full-index`.',
        'path': 'For local Git repositories, this should be the path to a '
                '.git directory that Review Board can read from. For remote '
                'Git repositories, it should be the clone URL.',
    pre_creation_regexp = re.compile("^0+$")
        preamble = ''
                    preamble = ''
                preamble = ''
                preamble += self.lines[i] + '\n'
        if self.lines[linenum].startswith("diff --git"):
        empty_change = self._is_empty_change(linenum)
        empty_change_linenum = linenum + GIT_DIFF_EMPTY_CHANGESET_SIZE

        file_info.data = self.lines[linenum] + "\n"
            file_info.origFile = GIT_DIFF_PREFIX.sub("", diff_line[-2])
            file_info.newFile = GIT_DIFF_PREFIX.sub("", diff_line[-1])
            file_info.data += self.lines[linenum] + "\n"
            file_info.data += self.lines[linenum] + "\n"
            file_info.data += self.lines[linenum] + "\n"
            file_info.data += self.lines[linenum + 1] + "\n"
            file_info.data += self.lines[linenum] + "\n"
            file_info.data += self.lines[linenum + 1] + "\n"
            file_info.data += self.lines[linenum + 2] + "\n"
            file_info.data += self.lines[linenum] + "\n"
            file_info.data += self.lines[linenum + 1] + "\n"
            file_info.data += self.lines[linenum + 2] + "\n"
        # Only show interesting empty changes. Basically, deletions.
        # It's likely a binary file if we're at this point, and so we want
        # to process the rest of it.
        if (empty_change and not file_info.deleted and not file_info.moved and
            not file_info.copied):
            return empty_change_linenum, None
            file_info.data += self.lines[linenum] + "\n"
                return linenum, file_info

            if self._is_binary_patch(linenum):
                file_info.data += self.lines[linenum] + "\n"
                return linenum + 1, file_info

            if self._is_diff_fromfile_line(linenum):
                if self.lines[linenum].split()[1] == "/dev/null":
            file_info.data += self.lines[linenum] + "\n"
            linenum += 1
    def _is_empty_change(self, linenum):
        next_diff_start_linenum = linenum + GIT_DIFF_EMPTY_CHANGESET_SIZE

        if next_diff_start_linenum >= len(self.lines):
            return True

        next_diff_start = self.lines[next_diff_start_linenum]
        next_line = self.lines[linenum + 1]
        return ((next_line.startswith("new file mode") or
                 next_line.startswith("old mode") or
                 next_line.startswith("deleted file mode"))
                and next_diff_start.startswith("diff --git"))

        return self.lines[linenum].startswith("new file mode")
        return self.lines[linenum].startswith("deleted file mode")
        return (self.lines[linenum].startswith("old mode")
                and self.lines[linenum + 1].startswith("new mode"))
        return (self.lines[linenum].startswith('similarity index') and
                self.lines[linenum + 1].startswith('copy from') and
                self.lines[linenum + 2].startswith('copy to'))
        return (self.lines[linenum].startswith("similarity index") and
                self.lines[linenum + 1].startswith("rename from") and
                self.lines[linenum + 2].startswith("rename to"))
                self.lines[linenum].startswith("index "))
        return self.lines[linenum].startswith('diff --git')
        return (line.startswith("Binary file") or
                line.startswith("GIT binary patch"))
                (self.lines[linenum].startswith('--- ') and
                    self.lines[linenum + 1].startswith('+++ ')))
        """
        This is needed so that there aren't explosions higher up
        the chain when the web layer is expecting a string object.
                setattr(file_info, attr, '')
        url_parts = urlparse.urlparse(self.path)
        url = url.replace("<filename>", urllib_quote(path))
        errmsg = p.stderr.read()
                raise SCMError("path must be supplied if revision is %s" % HEAD)
            return str(revision)
        url_parts = urlparse.urlparse(path)