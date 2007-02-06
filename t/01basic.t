#!/usr/bin/perl

use strict;
use warnings;

use Test::More tests => 2;

BEGIN {
    use_ok("Palm::Keyring", 0.93);
    use_ok("Wx", 0.67);
}
