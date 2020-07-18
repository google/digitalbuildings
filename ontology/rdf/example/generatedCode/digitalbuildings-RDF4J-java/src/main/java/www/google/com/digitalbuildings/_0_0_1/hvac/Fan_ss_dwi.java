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
* Class Fan_ss_dwi 
* Dishwasher-interlocked fan.
*/
@SuppressWarnings("serial")
public class Fan_ss_dwi extends www.google.com.digitalbuildings._0_0_1.hvac.Ss implements IFan_ss_dwi{

	IRI newInstance;
	public Fan_ss_dwi(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_ss_dwi"));
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

	public static Set<IFan_ss_dwi> getAllFan_ss_dwisObjectsCreated(){
		Set<IFan_ss_dwi> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_ss_dwi")).subjects().stream()
		.map(mapper->(IFan_ss_dwi)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}