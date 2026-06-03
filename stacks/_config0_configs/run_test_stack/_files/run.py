"""
# Copyright (C) 2025 Gary Leong <gary@config0.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Automated-test stack fixture (group2). Composes the group1 run_terraform
# execgroup, the group0 resource_wrapper.sh script, and the vpc_substack
# sub-stack via williaumwu FQNs. No selectors, no credentials — it only
# needs to exercise the scan passes.
"""

def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    # required variables
    stack.parse.add_required(key="resource_name",
                             types="str")

    stack.parse.add_required(key="aws_default_region",
                             types="str")

    # optional variables
    stack.parse.add_optional(key="tf_runtime",
                             types="str",
                             default="tofu:1.9.1")

    stack.parse.add_optional(key="region",
                             types="str",
                             default="us-east-1")

    # cross-repo dependencies (no credentials required for the scan passes)
    stack.add_execgroup("williaumwu:::config0-automated-test-group1::run_terraform")
    stack.add_script("williaumwu:::config0-automated-test-group0::resource_wrapper.sh")
    stack.add_substack("williaumwu:::config0-automated-test-substack::vpc_substack")

    # initialize
    stack.init_variables()
    stack.init_execgroups()

    return stack.get_results()
