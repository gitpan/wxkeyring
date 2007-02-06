# Makefile.PL for wxKeyring.

use ExtUtils::MakeMaker;

my @scripts = qw (wxkeyring);
my $usrbin = "/usr/bin";
my $installscript = $Config{installscript};

print STDERR <<EOD unless $installscript eq $usrbin;

WARNING: This Makefile will install user accessible scripts.
The location for these scripts is $installscript.
You may consider to pass INSTALLSCRIPT=$usrbin (or some other
convenient location) to "make install".
EOD

my %ctl = (
    NAME		=> 'wxkeyring',
    VERSION_FROM	=> 'script/'.$scripts[0],
    EXE_FILES           => [ map { "script/$_" } @scripts ],
    PREREQ_PM		=> {
	'Palm::Keyring' => 0.93,
        'Wx'            => 0.67,
    },
);

if ( $] >= 5.005 ) {
    $ctl{ABSTRACT_FROM} = 'script/'.$scripts[0],
    $ctl{AUTHOR}        = 'JV';
}

WriteMakefile(%ctl);
