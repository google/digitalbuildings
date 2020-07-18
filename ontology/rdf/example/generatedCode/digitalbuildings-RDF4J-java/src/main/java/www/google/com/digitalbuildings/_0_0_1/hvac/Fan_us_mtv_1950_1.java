package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IDryer_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.Dryer_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IDryer_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.Dryer_run_status_2;

/**
* Class Fan_us_mtv_1950_1 
* Non-standard type for 1950
*/
@SuppressWarnings("serial")
public class Fan_us_mtv_1950_1 extends www.google.com.digitalbuildings._0_0_1.hvac.Fan_ss implements IFan_us_mtv_1950_1{

	IRI newInstance;
	public Fan_us_mtv_1950_1(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_us_mtv_1950_1"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesDryer_run_status_1 (IDryer_run_status_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDryer_run_status_1> getUsesDryer_run_status_1 (){
		Set<IDryer_run_status_1> UsesDryer_run_status_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Dryer_run_status_1) {
				UsesDryer_run_status_1.add((Dryer_run_status_1)action);
			}
		});
		return UsesDryer_run_status_1;
	}


  public void addUsesDryer_run_status_2 (IDryer_run_status_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDryer_run_status_2> getUsesDryer_run_status_2 (){
		Set<IDryer_run_status_2> UsesDryer_run_status_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Dryer_run_status_2) {
				UsesDryer_run_status_2.add((Dryer_run_status_2)action);
			}
		});
		return UsesDryer_run_status_2;
	}

	public static Set<IFan_us_mtv_1950_1> getAllFan_us_mtv_1950_1sObjectsCreated(){
		Set<IFan_us_mtv_1950_1> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_us_mtv_1950_1")).subjects().stream()
		.map(mapper->(IFan_us_mtv_1950_1)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}