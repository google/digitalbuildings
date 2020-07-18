package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IDishwasher_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Dishwasher_run_status;

/**
* Class Fan_us_svl_mp7_2 
* Non-standard type for MP7
*/
@SuppressWarnings("serial")
public class Fan_us_svl_mp7_2 extends www.google.com.digitalbuildings._0_0_1.hvac.Fan_ss_vsc implements IFan_us_svl_mp7_2{

	IRI newInstance;
	public Fan_us_svl_mp7_2(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_us_svl_mp7_2"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesDishwasher_run_status (IDishwasher_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDishwasher_run_status> getUsesDishwasher_run_status (){
		Set<IDishwasher_run_status> UsesDishwasher_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Dishwasher_run_status) {
				UsesDishwasher_run_status.add((Dishwasher_run_status)action);
			}
		});
		return UsesDishwasher_run_status;
	}

	public static Set<IFan_us_svl_mp7_2> getAllFan_us_svl_mp7_2sObjectsCreated(){
		Set<IFan_us_svl_mp7_2> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_us_svl_mp7_2")).subjects().stream()
		.map(mapper->(IFan_us_svl_mp7_2)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}