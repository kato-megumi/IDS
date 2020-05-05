
allow = ["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment",
		"urgent","count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate",
		"same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count",
		"dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate",
		"dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate",
		"dst_host_rerror_rate","dst_host_srv_rerror_rate"]

select=['duration','protocol_type', 'serror_rate', 'srv_serror_rate',
		'same_srv_rate','srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count','dst_host_same_srv_rate',
		'dst_host_srv_diff_host_rate','dst_host_serror_rate', 'dst_host_srv_serror_rate']


attack_type_dict = {'back':'dos','land':'dos','neptune':'dos','pod':'dos','smurf':'dos','teardrop':'dos',
					'mailbomb':'dos','processtable':'dos','udpstorm':'dos','apache2':'dos','worm':'dos',
					'satan':'probe','ipsweep':'probe','nmap':'probe','portsweep':'probe','mscan':'probe',
					'saint':'probe','guess_passwd':'r2l','ftp_write':'r2l','imap':'r2l','phf':'r2l',
					'multihop':'r2l','warezmaster':'r2l','xlock':'r2l','xsnoop':'r2l','snmpguess':'r2l',
					'snmpgetattack':'r2l','httptunnel':'r2l','sendmail':'r2l','named':'r2l','spy':'r2l',
					'warezclient': 'r2l','buffer_overflow':'u2r','loadmodule':'u2r','rootkit':'u2r','perl':'u2r'
					,'sqlattack':'u2r','xterm':'u2r','ps':'u2r','normal': 'normal'}

feature = ["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent",
		"hot","num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root",
		"num_file_creations","num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login",
		"count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate",
		"diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate",
		"dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate",
		"dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate","label","score"]
