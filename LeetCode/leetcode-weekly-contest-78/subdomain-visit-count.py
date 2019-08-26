class Solution:

    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        domains = collections.Counter()
        subDomains = collections.Counter()

        # O(N)
        for item in cpdomains:
            count, domain = item.split(' ')
            subs = domain.split('.')
            for index in range(len(subs)):
                domains['.'.join(subs[index:])] += int(count)

        return ["{} {}".format(count, domain) for domain, count in domains.items()]
